from kfp import dsl
from kfp import compiler

@dsl.component(
    base_image='nvcr.io/nvidia/pytorch:26.01-py3'
)
def benchmark(n: int = 4096) -> str:
    import torch
    import numpy as np
    import time
    logs = ''

    logs += f'torch version: {torch.__version__}\n'
    logs += f'cuda available: {torch.cuda.is_available()}\n'

    if torch.cuda.is_available():
        logs += f'gpu count: {torch.cuda.device_count()}\n'
        logs += f'current device: {torch.cuda.current_device()}\n'
        logs += f'device name: {torch.cuda.get_device_name(0)}\n'
    else:
        logs += 'No GPU detected by PyTorch\n\n'

    # benchmark
    logs += f'Benchmark de multiplicação de matrizes {n} x {n}\n'
    a_cpu = np.random.rand(n, n).astype(np.float32)
    b_cpu = np.random.rand(n, n).astype(np.float32)

    # medição do tempo da CPU
    start_cpu = time.perf_counter()
    c_cpu = a_cpu @ b_cpu
    end_cpu = time.perf_counter()
    cpu_time = end_cpu - start_cpu
    logs += f'Tempo CPU (NumPy): {cpu_time:.4f} s\n'
        
    assert torch.cuda.is_available(), 'CUDA não disponível'
    device = torch.device('cuda')
    a_gpu = torch.randn(n, n, device=device)
    b_gpu = torch.randn(n, n, device=device)

    # aquecimento
    for _ in range(3):
        _ = a_gpu @ b_gpu
    torch.cuda.synchronize()

    # medição do tempo da GPU
    start_gpu = time.perf_counter()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    end_gpu = time.perf_counter()
    gpu_time = end_gpu - start_gpu
    logs += f'Tempo GPU (CUDA): {gpu_time:.4f} s\n'
    
    logs += f'Speedup GPU vs CPU: {cpu_time / gpu_time:.2f}x\n'

    return logs


@dsl.pipeline(
    name='gpu-check-pipeline',
    description='Pipeline KFP v2 para verificação de visibilidade das GPUs'
)
def check_gpu_pipeline() -> str:
    benchmark_task = benchmark()
    benchmark_task.set_accelerator_type('nvidia.com/gpu')
    benchmark_task.set_accelerator_limit(16)

    return benchmark_task.output


if __name__ == '__main__':
    compiler.Compiler().compile(
        pipeline_func=check_gpu_pipeline,
        package_path='gpu_cpu_benchmark.yaml'
    )