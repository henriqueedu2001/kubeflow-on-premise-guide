# ImagePullBackOff
Esse erro geralmente acontece porque ele não está conseguindo puxar ou achar a imagem para colocar no pod. As vezes essa imagem foi trocada de lugar ou simplesmente virou obsoleta.

## Como arrumar
Esse erro é bem chato de arrumar, então eu indicaria pra você refazer a instalação. Mas caso queira tentar arrumar um dos passos que fizemos e deu certo foi mexer no próprio yaml do 
pod mudando o lugar que faz o pull da imagem. 
Cada tipo de imagem é puxada de algum lugar então não tem como falarmos de onde você deve puxar a nova imagem será tudo na base de pesquisas. 



**RECOMENDAMOS A REINSTALAÇÃO DO CLUSTER E KUBEFLOW!!**
