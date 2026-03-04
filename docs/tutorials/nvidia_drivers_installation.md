# Instalação dos Drivers NVIDIA no Linux

Este guia explica como instalar os drivers proprietários da **NVIDIA** em um ambiente Linux, cobrindo os métodos mais comuns: via repositório da distribuição e via instalador oficial.

Recomenda-se sempre preferir os pacotes da própria distribuição antes de usar o instalador `.run` da NVIDIA.

## Verificar sua GPU

Primeiro, confirme se você possui uma GPU NVIDIA:

```bash
lspci | grep -i nvidia
```

Ou:

```bash
sudo lshw -C display
```


## Remover drivers antigos (se necessário)

Se já houver instalação anterior:

```bash
sudo apt remove --purge '^nvidia-.*'
sudo apt autoremove
```

Reinicie o sistema após a remoção.

## Ubuntu

```bash
sudo apt update
sudo apt upgrade
```

Ver drivers recomendados

```bash
ubuntu-drivers devices
```

### 3. Instalar automaticamente o recomendado

```bash
sudo ubuntu-drivers autoinstall
```

Ou instalar versão específica:

```bash
sudo apt install nvidia-driver-535
```

### 4. Reiniciar

```bash
sudo reboot
```

### 5. Verificar instalação

```bash
nvidia-smi
```

# Verificação Final

Após reiniciar:

```bash
nvidia-smi
```

Se estiver funcionando, você verá:

* Modelo da GPU
* Versão do driver
* Versão do CUDA
* Processos usando a GPU


# Problemas comuns

### Tela preta após reboot

Tente iniciar com:

```bash
nomodeset
```

Ou reinstalar o driver.