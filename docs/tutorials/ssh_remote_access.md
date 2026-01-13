# Tutorial - Acesso remoto via SSH
Considerando que o ambiente de alto desempenho, no qual desejamos executar o Kubeflow, seja acessível apenas remotamente, este tutorial elucida como fazer o acesso SSH, como configurar as chaves, para maior segurança, e como fazer um túnel SSH, para acessar portas.

# Requisito de rede
Para acessar remotamente uma determinada máquina, é preciso que (a) você, o cliente, e a máquina, o servidor (host), estejam numa mesma rede local, (b) a máquina servidora tenha um IP público ou (c) exista uma VPN (Virtual Private Network) que te permita estar numa mesma rede que a máquina servidora. Isso porque o acesso SSH necessita do endereço IP da máquina a ser acessada, sendo tal IP ou público, exposto à internet, ou visível dentro da mesma rede, mesmo que com VPN. Em qualquer um dos três exemplos, há um IP associado, que será utilizado no acesso descrito nos passos a seguir.

# SSH
O SSH é um protocolo para acesso remoto seguro a outra máquina pela rede, que fornece autenticação, criptografia de todo o tráfego, execução de comandos e transferência de arquivos com segurança. É amplamente usado para administrar servidores Linux, mas também funciona no Windows.

## Conexão SSH no Linux/Windows
No Linux ou no Windows, abra o terminal de comando. No windows, recomenda-se o PowerShell como terminal.

Em seguida, execute o comando de acesso SSH.
```bash
ssh <user>@<ip_addr>
```

Em que `user` é o usuário e `ip_addr` é o endereço IP do servidor.

Se o servidor expõe uma determinada porta `port` para acessá-lo via SSH, deve-se usar o comando abaixo.
```bash
ssh -p <port> <user>@<ip_addr>
```

Após dar o comando, digite a senha e pressione enter. Assim, você acessará um terminal remoto, da máquina servidora (host).

Quando desejar sair, dê o comando
```bash
exit
```

**Exemplo**: temos um servidor no IP público 143.107.112.549, na porta 2222, com user lmata e senha 11223344. Então, o acesso remoto SSH é feito com o comando abaixo.

```bash
ssh -p 2222 lmata@143.107.166.100
```

Depois, forneça a senha 11223344 e aperte enter.

# Túneis SSH/Port Forwarding
Um túnel SSH (ou port forwarding) permite encaminhar portas através de uma conexão SSH segura. Ele é usado para acessar serviços que não estão expostos à internet (ex.: banco de dados, painel web local)

```bash
ssh -p<port> -L <local_port>:<destiny>:<remote_port> <user>@<ip_addr>
```

Exemplo: temos uma máquina remota, no endereço de IP 192.168.5.7, na porta 22247, com user lmata. Nessa máquina, rodamos o Kubeflow, que utiliza a porta 8080. Desejamos acessar o Dashboard do Kubeflow na porta 3000 da nossa máquina local (localhost). Então, faremos forwarding da porta 8080 para a 3000 do localhost (é equivalente dizer que faremos um túnel SSH), com o seguinte comando.

```bash
ssh -p 22247 -L 3000:localhost:8080 lmata@192.168.5.7
```

Assim, podemos acessar o Dashboard do Kubeflow em nossa máquina local na porta 3000 do localhost. Essa porta nada mais é que a mesma porta 8080 da máquina remota.