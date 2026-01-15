# Tutorial - Instalação Docker
Docker é uma ferramenta que nos permite executar aplicações em contêineres.

## Instalação 

remover versões antigas
```
sudo apt remove docker docker-engine docker.io containerd runc
```

configurar repositório
```
sudo apt update
sudo apt install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

adicionar repositório docker 
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

instalar docker engine
```
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

permitir rodar docker sem sudo 
```
sudo usermod -aG docker $USER
```
REINICIE O SISTEMA!!!!

teste de funcionamento
```
docker run hello-world
```
O retorno será um Hello World e a criação de um conteiner.

(Caso tenha algum erro na hora de tentar rodar o teste utilize o comando sudo ou volte para o Passo anterior ao Teste)
[Video Tutorial Docker](https://www.youtube.com/watch?v=lRnCN475cto)
