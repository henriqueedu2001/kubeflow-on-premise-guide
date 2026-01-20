# Comandos do Kubectl
Este tutorial condensa os principais comandos do `kubectl`, a CLI (Command Line Interface) por meio da qual podemos interagir com clusters kubernetes.

# Informações básicas do Cluster

Utilize o comando

```bash
kubectl cluster-info
```

para ver informações básicas do cluster.

```bash
Kubernetes control plane is running at https://127.0.0.1:46693
CoreDNS is running at https://127.0.0.1:46693/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

Para mais verbosidade, acrescente a opção `dump`

```bash
kubectl cluster-info dump
```

Que gera uma saída bem completa sobre o cluster.

```
{
    "kind": "NodeList",
    "apiVersion": "v1",
    "metadata": {
        "resourceVersion": "23298553"
    },
    "items": [
        {
            "metadata": {
                "name": "kubeflow-control-plane",
                "uid": "d6dba54a-63b9-40cd-accb-a7db96096c13",
                "resourceVersion": "23297260",
                "creationTimestamp": "2025-12-01T12:16:58Z",
                "labels": {
                    "beta.kubernetes.io/arch": "amd64",
                    "beta.kubernetes.io/os": "linux",
                    "kubernetes.io/arch": "amd64",
                    "kubernetes.io/hostname": "kubeflow-control-plane",
                    "kubernetes.io/os": "linux",
                    "node-role.kubernetes.io/control-plane": ""
                },
                "annotations": {
...
```

Você pode verificar as versões do cliente e do servidor por meio do comando

```bash
kubectl version
```

Que gera como saída algo como

```bash
Client Version: v1.31.0
Kustomize Version: v5.4.2
Server Version: v1.31.0
```

Além disso, pode-se verificar os status dos componentes do control plane do cluster com o comando

```bash
kubectl get componentstatuses
```

Que gera como saída

```bash
NAME                 STATUS    MESSAGE   ERROR
controller-manager   Healthy   ok        
scheduler            Healthy   ok        
etcd-0               Healthy   ok  
```

# Namespaces
Namespaces são uma forma de isolar e organizar grupos recursos em um único cluster kubernetes. Dessa forma, por exemplo, podemos ter várias aplicações rodando num mesmo cluster, mas com cada uma isolada em um espaço lógico, identificado por um nome. 

## Visualização de Namespaces
Para visualisar os namespaces do cluster, utilize

```bash
kubectl get namespaces
```

O que gera como saída

```bash
NAME                        STATUS   AGE
auth                        Active   50d
cert-manager                Active   50d
default                     Active   50d
istio-system                Active   50d
knative-serving             Active   50d
kube-node-lease             Active   50d
kube-public                 Active   50d
kube-system                 Active   50d
kubeflow                    Active   50d
kubeflow-system             Active   50d
kubeflow-user-example-com   Active   50d
local-path-storage          Active   50d
oauth2-proxy                Active   50d
```

## Criação de Namespaces
Para criar um novo namespace, utilize o comando

```bash
kubectl create namespace <namespace_name>
```

Em que `namespace_name` é o nome do seu novo namespace. Em seguida, verifique se o namespace consta no cluster, com o comando de [visualização de namespaces](#visualização-de-namespaces).

## Deleção de Namespaces

```bash
kubectl delete namespace <namespace_name>
```

Em que `namespace_name` é o nome do seu novo namespace. Em seguida, verifique se o namespace está removido do cluster, com o comando de [visualização de namespaces](#visualização-de-namespaces).

# Recursos
Os recursos do cluster incluem pods, services, deployments e nodes.

## Visualização dos Pods de um Namespace
Cada namespace pode ter vários Pods. Para ver os Pods de um dado namespace, utilize o comando

```bash
kubectl get pods -n <namespace_name>
```

Em que `namespace_name` é o nome do namespace. Caso queira ver todos os Pods, independentemente de namespace, utilize o comando

```bash
kubectl get pods -A
```

**Exemplo**: para ver os pods do namespace `kubeflow`, utilize

```bash
kubectl get pods -n kubeflow
```

O que gera como saída

```bash
NAME                        STATUS   AGE
auth                        Active   50d
cert-manager                Active   50d
default                     Active   50d
istio-system                Active   50d
knative-serving             Active   50d
kube-node-lease             Active   50d
kube-public                 Active   50d
kube-system                 Active   50d
kubeflow                    Active   50d
kubeflow-system             Active   50d
kubeflow-user-example-com   Active   50d
local-path-storage          Active   50d
oauth2-proxy                Active   50d
```