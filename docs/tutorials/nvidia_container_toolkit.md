# Instalação do NVIDIA Container Toolkit no Ubuntu

Este guia explica como instalar o **NVIDIA Container Toolkit** no Ubuntu para permitir que containers (ex: Docker) utilizem a GPU NVIDIA.

> Pré-requisitos:
> - Driver NVIDIA instalado e funcionando (`nvidia-smi` deve funcionar)
> - Docker já instalado


## Verificar driver NVIDIA

Antes de tudo:

```bash
nvidia-smi
```

Se não funcionar, instale o driver antes de continuar.


## Instalar o Docker (caso ainda não tenha)

```bash
sudo apt update
sudo apt install docker.io
sudo systemctl enable --now docker
```

Teste:

```bash
docker run hello-world
```


## Adicionar repositório oficial NVIDIA

Adicionar chave GPG

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | \
sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
```

Adicionar repositório

```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) && \
curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```


Instalar o NVIDIA Container Toolkit

```bash
sudo apt update
sudo apt install -y nvidia-container-toolkit
```

Configurar o Docker para usar a NVIDIA e execute:

```bash
sudo nvidia-ctk runtime configure --runtime=docker
```

Reinicie o Docker:

```bash
sudo systemctl restart docker
```

## Testar acesso à GPU no container

Execute:

```bash
docker run --rm --gpus all nvidia/cuda:12.3.2-base-ubuntu22.04 nvidia-smi
```

Se tudo estiver correto, você verá a GPU listada dentro do container.

# Teste com PyTorch (opcional)

```bash
docker run --rm --gpus all pytorch/pytorch:latest \
python -c "import torch; print(torch.cuda.is_available())"
```

Deve imprimir:

```bash
True
```


# Problemas comuns

**Erro**: `could not select device driver "" with capabilities: [[gpu]]`

Verifique se:

* Docker foi reiniciado
* `nvidia-smi` funciona no host
* `nvidia-container-toolkit` está instalado