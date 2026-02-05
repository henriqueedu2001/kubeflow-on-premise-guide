import torch
import numpy as np
import time

def check_gpus():
    """Prints the available GPUs of your computational environment.

    Example::
        >>> check_gpus()
        CUDA isn\'t available

        >>> check_gpus()
        '''
        CUDA Available
        GPUs found: 1
        #1 GPU:
            - Name: NVIDIA GeForce RTX 4050 Laptop GPU
            - Capability: (8, 9)
            - Memory (GB): 5.64
        ...
        '''
    """
    # checks if CUDA is available
    if torch.cuda.is_available():
        print('CUDA Available')
    else:
        print('CUDA isn\'t available')
        return

    # prints the GPUs
    gpu_count = torch.cuda.device_count()
    print(f'GPUs found: {gpu_count}')
    for i in range(gpu_count):
        print(f'#{i + 1} GPU:')
        print(f'\t-Name: {torch.cuda.get_device_name(i)}')
        print(f'\t-Capability: {torch.cuda.get_device_capability(i)}')
        print(f'\t-Memory (GB): {round(torch.cuda.get_device_properties(i).total_memory / 1024**3, 2)}')
        print()


def benchmark(n: str = 8192):
    """Benchmarks the performance of the GPUs against the baseline of the CPU in multiplication of random
    matrices n x n.

    Args:
        n (str, optional): The size of the matrices. Defaults to 8192.
    
    Example:
        >>> benchmark()
        '''
        Benchmark: multiplication of random matrices 8192 x 8192
        CPU time: 2.2724 s
        GPU time: 0.1996 s
        Speedup GPU vs CPU: 11.39x
        Success: True
        '''
    """
    print(f'Benchmark: multiplication of random matrices {n} x {n}')
    if not torch.cuda.is_available():
        print('CUDA isn\'t available')
        return
    
    # matrices initialization
    a_cpu = np.random.rand(n, n).astype(np.float32)
    b_cpu = np.random.rand(n, n).astype(np.float32)

    # measuring the CPU time
    start_cpu = time.perf_counter()
    c_cpu = a_cpu @ b_cpu
    end_cpu = time.perf_counter()
    cpu_time = end_cpu - start_cpu
    print(f'CPU time: {cpu_time:.4f} s')
        
    device = torch.device('cuda')
    a_gpu = torch.randn(n, n, device=device)
    b_gpu = torch.randn(n, n, device=device)

    # GPU warm up
    for _ in range(3):
        _ = a_gpu @ b_gpu
    torch.cuda.synchronize()

    # measuring the GPUs time
    start_gpu = time.perf_counter()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    end_gpu = time.perf_counter()
    gpu_time = end_gpu - start_gpu
    print(f'GPU time: {gpu_time:.4f} s')
    
    # test resume
    print(f'Speedup GPU vs CPU: {cpu_time / gpu_time:.2f}x')
    print(f'Success: {gpu_time < cpu_time}')
    return


if __name__ == '__main__':
    check_gpus()
    benchmark()