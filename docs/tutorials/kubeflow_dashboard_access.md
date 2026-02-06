# Acesso ao Dashboard do Kubeflow
Se você estiver rodando o Kubeflow num servidor remoto, acesse-o via SSH fazendo port forwarding para a porta `8080`.

Por exemplo.

```bash
ssh -p12345 -L 8080:localhost:8080 myuser@192.168.1.2
```

Dentro do terminal do host, rode o comando abaixo.

```bash
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
```

Agora, o Dashboard do Kubeflow está disponível na porta `8080` do seu localhost. Para acessá-lo, entre na URL [http://localhost:8080](http://localhost:8080) usando seu navegador.

A tela de entrada irá exigir um login. Se você nunca o configurou, o usuário e a senha são do login padrão do Kubeflow.

- usuário: user@example.com
- senha: 12341234

Após isso, você acessará o Dashboard completo Kubeflow, com acesso aos pipelines, aos notebooks, etc.