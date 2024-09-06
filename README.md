# PiZero Industrial

## Introdução

Este repositório contem as instruções de instalação dos arquivos e bibliotecas para utilização do RS485 CAN HAT produzido pela Eneltec.

# Instalação

You can run ```sudo sh install.sh ``` or follow the steps:

## The shell via serial port must be disabled.

```sudo raspi-config``` > ```Interface Options``` > ```Serial Port``` > <No>

## CAN
1. Copie o seguinte texto para o arquivo em ``` /boot/firmware/config.txt``` (```/boot/config.txt``` para versões mais antigas do Raspbian)

```
dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=12
dtoverlay=spi-bcm2835-overlay

```

2. Para utilização do módulo CAN, usaremos a bibilioteca can-utils (https://elinux.org/Can-utils).
Instale utilizando o comando:

``` 
sudo apt-get install can-utils 

```

3.  Reboot.

4. Ative a interface com:

```
sudo ip link set can0 up type can bitrate 125000

```

5. Para enviar um frame utilizando a interface:
```
cansend can0 123#AAAA1010AAAA1010

```

Para realizar a leitura:

```
candump can0

```

## RS485


1. Set up respository and virtual environment:

```
sudo chmod +x .industrial/modbus.py
sudo python3 -m venv .industrial/.venv
```

2. Download the requeriments.

```
sudo .industrial/.venv/bin/pip install .industrial/requeriments.txt
```
or

```
sudo .industrial/.venv/bin/pip install pyserial==3.5
sudo .industrial/.venv/bin/pip install pymodbus==3.7.2
```

3. Create an alias and reaload the source file: 

```
echo alias modbus="'/home/eneltec/.industrial/.venv/bin/python3 /home/eneltec/.industrial/modbus.py'" | sudo tee -a ~/.bashrc
source ~/.bashrc
```

4. Test the Modbus Interface:

``` 
modbus read coil 1 1 1
```