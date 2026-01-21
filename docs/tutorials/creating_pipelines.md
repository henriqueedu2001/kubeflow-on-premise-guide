# Criação de Pipelines no Kubeflow
O Kubeflow Pipelines (KFP) é uma plataforma para criar, orquestrar e executar workflows de machine learning sobre Kubernetes. Ele permite definir pipelines reprodutíveis, versionáveis e escaláveis, cobrindo todo o ciclo de vida de ML: preparação de dados, treinamento, validação, deploy e monitoramento.

Um pipeline é um grafo direcionado acíclico (DAG) composto por componentes, onde cada componente representa uma etapa bem definida do fluxo. O Kubeflow cuida da execução, paralelização, cache, versionamento e rastreabilidade de cada execução.


# Criando Pipelines
A forma mais utilizada de criar pipelines é usando o SDK do Kubeflow Pipelines em python. A partir de um código python, que especifica um pipeline do kubeflow, o SDK gera o .yaml correspondente, processo ao qual damos o nome de compilação. Vamos mostrar aqui um exemplo de compilação para o pipeline `hello_world.py`, disponível em `src/pipelines/hello_world`.

O script python é o seguinte:

```python
from kfp import dsl
from kfp import compiler

@dsl.component
def say_hello(name: str) -> str:
    hello_text = f'Hello, {name}!'
    print(hello_text)
    return hello_text

@dsl.pipeline
def hello_pipeline(recipient: str) -> str:
    hello_task = say_hello(name=recipient)
    return hello_task.output

compiler.Compiler().compile(hello_pipeline, 'hello_world.yaml')
```

Temos aqui a especificação de um componente `say_hello` que possui como input uma string `name` e output uma string de saudações, por exemplo, "Hello, Henrique!" para `name='Henrique'`. Em seguida, especificamos um pipeline `hello_pipeline`, que recebe um input `recipient`, informado ao componente, e aproveita dele também o output.

Esse script é executável. A última linha realiza a compilação e gera um arquivo .yaml chamado `hello_world.yaml`, que é o pipeline compilado.

Para compilar o pipeline, instale o SDK no seu ambiente.

```bash
pip install kfp
```

Abra o diretório do pipeline hello_world:

```bash
cd src/pipelines/
```

Em seguida, execute o script.

```bash
python3 hello_world.py
```

Assim, você gerará o .yaml abaixo no diretório.

```yaml
# PIPELINE DEFINITION
# Name: hello-pipeline
# Inputs:
#    recipient: str
# Outputs:
#    Output: str
components:
  comp-say-hello:
    executorLabel: exec-say-hello
    inputDefinitions:
      parameters:
        name:
          parameterType: STRING
    outputDefinitions:
      parameters:
        Output:
          parameterType: STRING
deploymentSpec:
  executors:
    exec-say-hello:
      container:
        args:
        - --executor_input
        - '{{$}}'
        - --function_to_execute
        - say_hello
        command:
        - sh
        - -c
        - "\nif ! [ -x \"$(command -v pip)\" ]; then\n    python3 -m ensurepip ||\
          \ python3 -m ensurepip --user || apt-get install python3-pip\nfi\n\nPIP_DISABLE_PIP_VERSION_CHECK=1\
          \ python3 -m pip install --quiet --no-warn-script-location 'kfp==2.15.2'\
          \ '--no-deps' 'typing-extensions>=3.7.4,<5; python_version<\"3.9\"' && \"\
          $0\" \"$@\"\n"
        - sh
        - -ec
        - 'program_path=$(mktemp -d)


          printf "%s" "$0" > "$program_path/ephemeral_component.py"

          _KFP_RUNTIME=true python3 -m kfp.dsl.executor_main                         --component_module_path                         "$program_path/ephemeral_component.py"                         "$@"

          '
        - "\nimport kfp\nfrom kfp import dsl\nfrom kfp.dsl import *\nfrom typing import\
          \ *\n\ndef say_hello(name: str) -> str:\n    hello_text = f'Hello, {name}!'\n\
          \    print(hello_text)\n    return hello_text\n\n"
        image: python:3.11
pipelineInfo:
  name: hello-pipeline
root:
  dag:
    outputs:
      parameters:
        Output:
          valueFromParameter:
            outputParameterKey: Output
            producerSubtask: say-hello
    tasks:
      say-hello:
        cachingOptions:
          enableCache: true
        componentRef:
          name: comp-say-hello
        inputs:
          parameters:
            name:
              componentInputParameter: recipient
        taskInfo:
          name: say-hello
  inputDefinitions:
    parameters:
      recipient:
        parameterType: STRING
  outputDefinitions:
    parameters:
      Output:
        parameterType: STRING
schemaVersion: 2.1.0
sdkVersion: kfp-2.15.2
```

Este yaml está pronto para ser executado, bastando submetê-lo a qualquer backend de Kubeflow.