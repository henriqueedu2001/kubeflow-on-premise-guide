# Tutorial - Instalação Kubectl
Kubectl é uma ferramenta de linha de comando para controlar cluster Kubernetes

## Instalação 

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

verificar instalação
```
kubectl version --client
```

[Video tutorial instalação Kubectl](https://www.youtube.com/watch?v=tqLUauXS-VA)
