# Tutorial - Instalação Helm
Helm é um gerenciador de pacotes para Kubernetes, que simplifica a definição, instalação e gerenciamento de aplicações complexas, agrupando todos os 
recursos necessários (manifestos YAML) em um único pacote reutilizável chamado Helm Chart

## Instalação 
```
curl -Lo helm.tar.gz https://get.helm.sh/helm-v3.13.1-linux-amd64.tar.gz
tar -zxvf helm.tar.gz
sudo mv linux-amd64/helm /usr/local/bin/helm
```

verificar instalação 
```
helm version
```
