# Tutorial - Instalação e acesso ao Kubeflow
Antes de começarmos a instalação do `kubeflow` é necessário realizar a seguinte etapa [instalação do nvkind](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/nvkind_installation.md).

`Kubeflow` é uma plataforma de código aberto para orquestrar, implantar e gerenciar fluxos de trabalho de Machine Learning (ML) no kubernetes, tornando o ML escalável.

## Requisitos para instalação
Para a instalação e configuração do `kubeflow` nós temos algum pré-requisitos, sendo eles:

| Pré-requisitos | Link | 
| --------- | ----- | 
| docker    | [instalação do docker](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/docker_installation.md) | 
| kind      | [instalação do kind](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kind_installation.md) | 
| kubectl   | [instalação do kubectl](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kubectl_installation.md) | 
| kustomize | [instalação do kustomize](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kustomize_installation.md) |

## Clone este repositório em seu diretório
```bash
git clone https://github.com/henriqueedu2001/kubeflow-on-premise-guide
```

## Instalar drivers da NVIDIA
Instale os drivers da NVIDIA na sua máquina usando as instruções [deste tutorial](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/nvidia_drivers_installation.md)

## Instalação do Docker
Instale o docker na sua máquina usando as instruções [deste tutorial](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/docker_installation.md)

## Instale o NVIDIA Container Toolkit
Instale o docker na sua máquina usando as instruções [deste tutorial](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/nvidia_container_toolkit.md).

Certifique-se de que as GPUs estejam visíveis para o container docker.

## Instale o Kubectl
Instale o Kubectl na sua máquina usando as instruções [deste tutorial](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kubectl_installation.md).

## Instale o Kind
Instale o Kind na sua máquina usando as instruções [deste tutorial](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kind_installation.md).

## Instale o Helm
Instale o Helm na sua máquina usando as instruções [deste tutorial](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/helm_installation.md).

## Instale o NVIDIA GPU OPERATOR
Ative as GPUs com NVIDIA GPU OPERATOR, seguindo à risca [este tutorial](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/enabling_gpus.md).

## Instale o Kustomize
Instale o Kustomize na sua máquina usando as instruções [deste tutorial](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kustomize_installation.md).

## Instalação 
Clone repositório do **`kubeflow`**
```
git clone https://github.com/kubeflow/manifests.git
cd manifests
```

Instalar a plataforma
```bash
while ! kustomize build example | kubectl apply --server-side --force-conflicts -f -; do
  echo "Retrying to apply resources"
  sleep 20
done
```

Este comando demora, então aguarde cerca de 10 min. Após verifique os pods com o comando:

```bash
kubectl get pods -A
```

Caso tenha algum pod com Creating, CrashLoopBackOf ou algo semelhante espere alguns minutos para eles se normalizarem !!