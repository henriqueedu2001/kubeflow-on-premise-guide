# Problemas de Instalação com SNAP
Na instalação de cada um dos requisitos evite de instalar através do **snap**, pois a instalação não vem corretamente.

## Motivos
O **snap** executa aplicações dentro de um **SandBox** usando algumas bibliotecas e ferramentas. Em uma **VM** esse isolamento se torna um problema.
- A VM já está isolada do host
- O Snap cria uma segunda camada de isolamento
- Recursos de baixo nível ficam inacessíveis

Como resultado recursos ficam indisponíveis como: Drivers, GPUs, Recursos do Kernel ficam indisponíveis 

## Intalações já feitas com SNAP
Caso você já tenha feito a instalação dos recursos utilizando o **snap**, o recomendado é fazer a desinstalação e seguir os passos corretos que estão localizados em [Tutorial](https://github.com/henriqueedu2001/kubeflow-on-premise-guide/tree/main/docs/tutorials)
