# Gerenciando clusters Kubernetes com kind e kubectl
Este documento mostra os principais comandos para criar, listar e deletar clusters kind utilizando tanto o próprio kind quanto o kubectl.

# Criando um cluster kind
Há três formas de criar um cluster no kind: (1) criação simples, (2) criação com nome e (3) criação a partir de um arquivo YAML de configuração.

## Criação simples (cluster padrão)
Para criar um cluster com as configurações padrão, rode o comando abaixo.

```bash
kind create cluster
```

Ele cria um cluster chamado `kind` e um nó do tipo control-plane.

## Criando um cluster com nome específico
Para criar um cluster com um nome específico, rode o comando abaixo.

```bash
kind create cluster --name <cluster_name>
```

Sendo `cluster_name` o nome do cluster escolhido. Esse nome será usado para identificar o cluster em comandos futuros.

## Criando um cluster a partir de um arquivo YAML
Para criar um cluster partindo de um arquivo de configuração `cluster.yaml`, você deve rodar o comando abaixo.

```bash
kind create cluster --config <config_yaml_path>
```

É possível também adicionar um nome para o cluster, com a flag `--name`.

```bash
kind create cluster --name <cluster_name> --config <config_yaml_path>
```

Em que `config_yaml_path` é o caminho para seu arquivo de configuração YAML.

Por exemplo, considere o arquivo `cluster.yaml` abaixo.

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
  extraMounts:
    - hostPath: /dev/null
      containerPath: /var/run/nvidia-container-devices/all
```

Para criar um cluster com a configuração desse yaml e o nome `my-cluster`, basta rodar o comando.

```bash
kind create cluster --name my-cluster --config ./cluster.yaml
```

# Listando clusters existentes
Para listar todos os clusters kind criados na máquina, rode o comando abaixo.

```bash
kind get clusters
```

Você obterá como saída uma lista com os nomes de todos os clusters kind criados na sua máquina.

Por exemplo

```text
kind
my-cluster
ci-test
```
``

# Deletando clusters
Há duas formas de deletar um cluster: (1) deleção do cluster padrão e (2) deleção de um cluster em específico.

Para deletar o cluster padrão (`kind`), rode o comando abaixo.

```bash
kind delete cluster
```

Para deletar um cluster específico, rode o comando abaixo.

```bash
kind delete cluster --name <cluster_name>
```

Em que `cluster_name` é o nome do cluster a ser deletado. Para verificar que a deleção foi bem sucedida, [liste os clusters](#listando-clusters-existentes) e veja se o nome sumiu da lista.