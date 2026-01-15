# Tutorial - Instalação do nvkind

O `nvkind` é uma ferramenta para criar e gerenciar `kind` clusters com acesso a GPUs. 

Rodar o `kind` padrão com acesso as GPUs não é muito simples. Não existe uma maneira padrão de injetar suporte a GPUs em um nós de trabalho do `kind` e mesmo que de 
pra usar algumas "gambiarras" para fazer isso se tornar possível ainda é necessário realizar algum pós-processamento para garantir que diferentes conjuntos de GPUs
ser isolados em diferentes nós de trabalho. 

O `nvkind` junto o conjunto de etapas que são precisas para fazer a criação de um nó com GPU. 

## Requisitos para instalação
Para a instalação e configuração do `nvkind` nós temos algum pré-requisitos, sendo eles: 

| Pré-requisitos | Link | 
| --------- | ----- | 
| Go        | [instalação go](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/go_installation.md) | 
| docker    | [instalação docker](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/docker_installation.md) | 
| kind      | [instalação kind](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kind_installation.md) | 
| kubectl   | [instalação kubectl](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kubectl_installation.md) | 
| heml      | [instalação helm](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/helm_installation.md) |
| kustomize | [instalação kustomize](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kustomize_installation.md) |

## Instalação 

### Instalação NVIDIA Toolkit

configração do repositório
```
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

instalação
```
sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
```

Configuração crítica (CDI e Runtime)
```
# Configura o Docker Runtime e habilita CDI
sudo nvidia-ctk runtime configure --runtime=docker --set-as-default --cdi.enabled

# Gera a especificação CDI para os dispositivos encontrados
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml

# Reinicia o Docker
sudo systemctl restart docker
```

### Instalação ferramentas de orquestração

Para o `kind` utilize o [tutorial kind](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kind_installation.md), `helm` o [tutorial helm](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/helm_installation.md) e `kustomize` o [tutorial kustomize](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kustomize_installation.md)

`Nvkind`
```
go install github.com/NVIDIA/nvkind/cmd/nvkind@latest
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc
source ~/.bashrc
```

### Criação do cluster e ativação da GPU

```
# Criar o cluster
nvkind cluster create --name kubeflow-gpu

# Validar se o nó worker enxerga a GPU
docker exec -it kubeflow-gpu-worker nvidia-smi
```
(Deve exibir a tabela com as duas Tesla T4/GPUs).

Instalação NVIDIA Operator </br>
Torna as GPU "agendáveis" pelo Kubernetes
```
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia && helm repo update

helm install gpu-operator nvidia/gpu-operator \
  -n gpu-operator --create-namespace \
  --set driver.enabled=false \
  --set toolkit.enabled=false
```

### Teste 
Para verificar se a gpu está sendo identificada rode o seguinte código
```
kubectl describe nodes | grep -A 5 "Capacity:"
```
deve conter uma linha parecida com está `nvidia.com/gpu: 1`
