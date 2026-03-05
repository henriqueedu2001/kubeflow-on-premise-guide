from kfp.dsl import component
from kfp.dsl import pipeline
from kfp import compiler


@component(
    base_image='ultralytics/ultralytics:latest'
)
def train_yolo_component():
    import json
    from pathlib import Path
    from ultralytics import YOLO
    model = YOLO('yolov8n.pt')
    dataset = 'coco8.yaml'

    model.train(
        data=dataset,
        epochs=10,
        imgsz=640,
        batch=16,
        project='runs',
        name='yolo_training_example'
    )

    model_path = Path('runs/detect/runs/yolo_training_example/weights/best.pt')

    trained_model = YOLO(model_path)

    metrics = trained_model.val()

    results = {
        'precision': float(metrics.box.mp),
        'recall': float(metrics.box.mr),
        'map50': float(metrics.box.map50),
        'map50_95': float(metrics.box.map),
    }

    print('\n=== MÉTRICAS ===')
    for k, v in results.items():
        print(f'{k}: {v:.4f}')

    with open('metrics.json', 'w') as f:
        json.dump(results, f, indent=4)

    print(f'\nModelo salvo em: {model_path}')
    print('Métricas salvas em: metrics.json')
    return


@pipeline(
    name='train-yolo-pipeline',
    description='Treinamento de YOLO'
)
def train_yolo_pipeline():
    task = train_yolo_component()


if __name__ == '__main__':
    compiler.Compiler().compile(
        pipeline_func=train_yolo_pipeline,
        package_path='train_yolo_pipeline.yaml'
    )