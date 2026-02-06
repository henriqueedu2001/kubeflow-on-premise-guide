# Alocando GPUs para clusters Kind
Antes de mais nada, **é importante saber que o Kubernetes *Kind*, por design, não tem suporte nativo ao passthrough de GPUs NVIDIA dentro dos nós do cluster**, porque os nós são containers Docker e não VMs/hosts reais com dispositivos PCI-e passados diretamente para eles. Algumas ferramentas experimentais e hacks existem (como nvkind), mas não há suporte oficial / estável para GPUs em Kind. ([GitHub][1])

No entanto, abaixo está um passo a passo **didático** cobrindo como checar dispositivos GPU no host e como instalar o **NVIDIA GPU Operator** em um cluster Kubernetes “real”, seguindo a *documentação oficial da NVIDIA*. ([NVIDIA Docs][2])


# 1. Verificações prévias no host (antes do Kubernetes)
Verifique se o host possui GPUs visíveis.

```bash
nvidia-smi -L
```

Verifique que o driver está instalado e vê as GPUs.

```bash
nvidia-smi
```

Teste se o docker consegue acessar as GPUs.

```bash
docker run --rm --gpus all nvidia/cuda:12.6.2-base-ubuntu22.04 nvidia-smi
```

Se isso falhar, o driver ou a NVIDIA Container Toolkit não está configurado corretamente.

Verifique se o Helm está instalado.

```bash
helm version
```

# 2. Configuração de um cluster Kubernetes
Crie um cluster kubernetes, utilizando o arquivo de configuração `/src/cluster.yaml`.

```bash
kind create cluster --config ./cluster.yaml
```

# 3. Instalação do NVIDIA GPU Operator com Helm

Adicione o repositório Helm da NVIDIA.

```bash
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm repo update
```

Crie o namespace com política privilegiada

```bash
kubectl create namespace gpu-operator
kubectl label namespace gpu-operator pod-security.kubernetes.io/enforce=privileged
```

Instale o GPU Operator

```bash
helm install --wait --generate-name \
  -n gpu-operator --create-namespace \
  nvidia/gpu-operator \
  --version=v25.10.1
```

Se os drivers já estiverem no host e você não quer que o operador tente instalá-los:

```bash
helm install --wait --generate-name \
  -n gpu-operator --create-namespace \
  nvidia/gpu-operator \
  --set driver.enabled=false
```

Esses comandos seguem o procedimento oficial de instalação do GPU Operator. ([NVIDIA Docs][2])

# 4. Verificação da instalação

Cheque os pods no namespace do operador.

```bash
kubectl get pods -n gpu-operator
```

Cheque os nós rotulados para GPUs.

```bash
kubectl get nodes --show-labels | grep nvidia
```

# 5. Testes
TODO

# 6. Observações

O NVIDIA GPU Operator automatiza drivers, device plugin e ferramentas essenciais para workloads com GPU. ([NVIDIA Docs][3])

O Kind por si só NÃO expõe GPUs reais para pods nativamente. A comunidade explorou hacks e projetos (como nvkind), mas eles não são parte do GPU Operator oficial e não há suporte estável no repositório principal. ([GitHub][1])

[1]: https://github.com/NVIDIA/nvkind?utm_source=chatgpt.com "NVIDIA/nvkind"
[2]: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html?utm_source=chatgpt.com "Installing the NVIDIA GPU Operator — NVIDIA GPU Operator"
[3]: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html?utm_source=chatgpt.com "About the NVIDIA GPU Operator"
