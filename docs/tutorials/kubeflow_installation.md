# Tutorial - Instalação e acesso ao Kubeflow
Antes de começarmos a instalação do `kubeflow` é necessário realizar a seguinte etapa [instalação do nvkind](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/nvkind_installation.md).

`Kubeflow` é uma plataforma de código aberto para orquestrar, implantar e gerenciar fluxos de trabalho de Machine Learning (ML) no kubernetes, tornando o ML escalável.

## Requisitos para instalação
Para a instalação e configuração do `kubeflow` nós temos algum pré-requisitos, sendo eles:

| Pré-requisitos | Link | 
| --------- | ----- | 
| nvkind    | [instalação do nvkind](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/nvkind_installation.md) | 
| docker    | [instalação do docker](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/docker_installation.md) | 
| kind      | [instalação do kind](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kind_installation.md) | 
| kubectl   | [instalação do kubectl](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kubectl_installation.md) | 
| kustomize | [instalação do kustomize](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/blob/main/docs/tutorials/kustomize_installation.md) | 

## Instalação 

Após a configuração do cluster com `nvkind` devemos clonar repositório do **`kubeflow`**
```
git clone https://github.com/kubeflow/manifests.git
cd manifests
```

Instalar a plataforma
```
while ! kustomize build example | kubectl apply --server-side --force-conflicts -f -; do
  echo "Retrying to apply resources"
  sleep 20
done
```
Este comando demora, então aguarde cerca de 10 min. Após verifique os pods com o comando:
```
kubectl get pods -A
```
Caso tenha algum pod com Creating, CrashLoopBackOf ou algo semelhante espere alguns minutos para eles se normalizarem !!

### Acesso a plataforma
Digite no terminal o seguinte código:
```
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
```

Entrar na URL do Kubeflow
```
http://localhost:8080
```
Nela irá pedir um usuário e uma senha 

- usuário: user@example.com
- senha: 12341234

Pronto agora já temos acesso completo a plataforma
