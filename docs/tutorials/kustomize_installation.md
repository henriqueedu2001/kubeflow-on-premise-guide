# Tutorial - Instalação Kustomize
Kustomize é uma ferramenta nativa do Kubernetes para personalizar arquivos de configuração YAWML sem usar modelos.

## Instalação 

baixar arquivo

```bash
curl -s https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh | bash
sudo mv kustomize /usr/local/bin/
kustomize version
```

mover para um local Global
```
sudo mv kustomize /usr/local/bin/
rm kustomize_linux_amd64.tar.gz
```

verificar instalação
```
kustomize version
```

[Chat tutorial instalação Kustomize](https://chatgpt.com/share/69416398-3044-8005-aa8b-24d26c3357a4)
