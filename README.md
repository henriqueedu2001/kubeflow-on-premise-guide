# Guia de uso do Kubeflow em ambiente on-premise
Este repositório contém documentação completa para instalação e uso do Kubeflow em ambientes computacionais de alto desempenho on-premise.

# Sobre
Guia desenvolvido por pesquisadores do Centro Interdisciplinar de Tecnologias Interativas da Universidade de São Paulo (CITI-USP), documentando o processo de implementação do Kubeflow no cluster ASIMOV para treinamento de modelos de visão computacional.

- **Henrique S. Souza** (`@henriqueedu2001`): Aluno de iniciação científica, Engenharia de computação - USP.
- **Vicente Pascoal** (`@Vicente-VP`): Estagiário, Análista e Desenvolvedor de Sistemas - FATEC.

# Estrutura do Repositório
```text
.
├── docs/
│   ├── tutorials/          # Tutoriais de instalação e configuração
│   ├── troubleshooting/    # Soluções para problemas comuns
│   └── img/                # Imagens utilizadas na documentação
├── src/
├── LICENSE
└── README.md
```

# Documentação 
#### `docs/tutorials/`
Contém tutoriais passo a passo para:

- Instalação completa do Kubeflow e suas dependências (Docker, kubectl, Kustomize, Kind)
- Configuração de acesso remoto via SSH
- Criação e execução de pipelines
- Operações comuns do servidor

#### `docs/troubleshooting/`
Soluções para problemas frequentes como:

- Erros de SSH
- Problemas com dependências do Kubeflow
- Erros de pull de imagens (ErrPullImage)
- CrashLoopBackOff em pods
- Requisitos de recursos computacionais

#### `docs/img/`
Imagens e capturas de tela utilizadas nos tutoriais e documentação.

# Pré-requisitos
Este guia assume que você possui:

- Máquina ou cluster com GPUs NVIDIA
- Acesso físico ou via SSH à máquina
- Recursos mínimos: 8 CPUs e 60GB RAM

# Como Usar Este Repositório
1. Navegue até docs/tutorials/ para seguir os guias de instalação
2. Consulte docs/troubleshooting/ caso encontre problemas durante a instalação ou uso
3. As imagens de referência estão disponíveis em docs/img/

# Contribuições
Desenvolvido como resultado de investigações práticas no uso do Kubeflow para MLOps no CITI-USP.
