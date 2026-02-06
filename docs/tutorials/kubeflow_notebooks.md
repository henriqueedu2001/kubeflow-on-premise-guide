# Criação de Notebooks no Kubeflow

O Kubeflow Notebooks é um recurso da plataforma Kubeflow que permite criar e gerenciar ambientes interativos de desenvolvimento baseados em Jupyter Notebooks sobre Kubernetes. Ele é amplamente utilizado para exploração de dados, prototipação de modelos, experimentação, análise exploratória (EDA) e desenvolvimento inicial de pipelines de machine learning.

Diferentemente do Kubeflow Pipelines, que foca em execução reprodutível e automatizada, os notebooks são ambientes interativos, ideais para iteração rápida, testes manuais e investigação de dados. Cada notebook roda em um pod isolado, com recursos (CPU, memória, GPU) configuráveis e acesso controlado a volumes persistentes.

# Conceitos Fundamentais

Um Notebook no Kubeflow é composto, conceitualmente, pelos seguintes elementos:

* **Imagem Docker**: define o ambiente (Python, bibliotecas, frameworks como PyTorch ou TensorFlow).
* **Servidor de Notebook**: normalmente JupyterLab ou Jupyter Notebook.
* **Volume Persistente (PVC)**: garante que arquivos, notebooks e resultados não sejam perdidos ao reiniciar o pod.
* **Recursos Computacionais**: CPU, memória e, opcionalmente, GPUs.
* **Configurações de Acesso**: controle de namespace, permissões e autenticação.

O Kubeflow gerencia o ciclo de vida desses notebooks, cuidando da criação, inicialização, reinício e exclusão dos pods associados.

# Criando Notebooks

A forma mais comum de criar notebooks é via interface web do Kubeflow (Kubeflow Central Dashboard). Também é possível criá-los programaticamente via manifests Kubernetes (YAML), o que é útil para versionamento e automação.

A seguir, apresentamos um exemplo conceitual de criação de um notebook chamado `hello_notebook`, utilizando uma imagem padrão de ciência de dados.

## Criação via Interface Web

1. Acesse o **Kubeflow Central Dashboard**.
2. Navegue até a seção **Notebooks**.
3. Clique em **New Notebook**.
4. Preencha os campos principais:

   * **Name**: `hello-notebook`
   * **Namespace**: seu namespace de trabalho
   * **Image**: por exemplo, `jupyter/scipy-notebook:python-3.11`
   * **CPU / Memory**: conforme a necessidade
   * **GPU** (opcional): selecione se necessário
   * **Workspace Volume**: defina ou reutilize um PVC
5. Clique em **Launch**.

Após alguns instantes, o notebook ficará disponível para acesso via JupyterLab.

## Estrutura de um Notebook

Uma vez criado, o notebook funciona como um ambiente Jupyter padrão. Por exemplo, um notebook simples pode conter a seguinte célula de código:

```python
print('Hello, Kubeflow Notebook!')
```

Esse código é executado dentro do pod Kubernetes associado ao notebook, utilizando os recursos previamente configurados.

# Criação via YAML

Assim como pipelines, notebooks também podem ser descritos em YAML. No Kubeflow, isso é feito através do recurso customizado `Notebook` (CRD) do Kubernetes.

Abaixo está um exemplo simplificado de manifesto YAML para criação de um notebook:

```yaml
apiVersion: kubeflow.org/v1
kind: Notebook
metadata:
  name: hello-notebook
  namespace: ml-workspace
spec:
  template:
    spec:
      containers:
        - name: notebook
          image: jupyter/scipy-notebook:python-3.11
          resources:
            requests:
              cpu: "1"
              memory: "2Gi"
            limits:
              cpu: "2"
              memory: "4Gi"
          volumeMounts:
            - name: workspace-volume
              mountPath: /home/jovyan
      volumes:
        - name: workspace-volume
          persistentVolumeClaim:
            claimName: hello-notebook-pvc
```

Esse manifesto define:

* O nome e namespace do notebook
* A imagem Docker utilizada
* Recursos mínimos e máximos
* Um volume persistente montado no diretório de trabalho do usuário

Para criar o notebook, basta aplicar o manifesto:

```bash
kubectl apply -f hello_notebook.yaml
```

# Persistência e Versionamento

Os notebooks utilizam Persistent Volume Claims (PVCs), garantindo que arquivos e resultados sejam preservados mesmo que o pod seja reiniciado ou recriado. É uma boa prática:

* Manter notebooks organizados por projeto
* Versionar notebooks importantes em Git
* Separar código experimental de código produtivo

# Boas Práticas

* Utilize notebooks para **exploração e prototipação**, não para execução em produção.
* Extraia código estável para **pipelines Kubeflow** ou scripts versionados.
* Defina limites de recursos para evitar consumo excessivo do cluster.
* Prefira imagens customizadas quando precisar de dependências específicas.

# Integração com Pipelines

Notebooks e pipelines são complementares. Um fluxo comum é:

1. Explorar dados e testar ideias em notebooks
2. Consolidar código em componentes reutilizáveis
3. Criar pipelines Kubeflow para execução automatizada e reprodutível

Dessa forma, os notebooks funcionam como o ambiente de pesquisa e desenvolvimento, enquanto os pipelines cuidam da operacionalização.

Esse notebook está pronto para ser utilizado como ambiente interativo dentro de qualquer cluster Kubeflow configurado corretamente.
