# PiZero Industrial

## Introduction

This repository contains the installation instructions for the RS485 CAN HAT produced by Eneltec.
Clone this repository with

```
sudo apt -y update
sudo apt -y upgrade
sudo apt install git -y
git clone https://github.com/ENELTEC/PiZero-Industrial.git industrial

```

# Install

ATENTION: The shell via serial port must be disabled.

You can run ```sudo sh install.sh ``` or follow the steps:


```sudo raspi-config``` > ```Interface Options``` > ```Serial Port``` > ```No```

## CAN
1. Copy the following text to the file at ``` /boot/firmware/config.txt``` (```/boot/config.txt``` for older versions of Raspbian)

```
dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=12
dtoverlay=spi-bcm2835-overlay

```

2. To use the CAN module, we will use the can-utils library (https://elinux.org/Can-utils). Install it using the command:

``` 
sudo apt-get install can-utils 

```

3.  Reboot.

4. Activate the interface with:

```
sudo ip link set can0 up type can bitrate 125000

```

5. To send a frame with the interface:
```
cansend can0 123#AAAA1010AAAA1010

```

To read:

```
candump can0

```

## RS485


1. Set up respository and virtual environment:

```
sudo chmod +x industrial/modbus.py
sudo python3 -m venv industrial/.venv
```

2. Download the requeriments.

```
sudo industrial/.venv/bin/pip install industrial/requeriments.txt
```
or

```
sudo industrial/.venv/bin/pip install pyserial==3.5
sudo industrial/.venv/bin/pip install pymodbus==3.7.2
```

3. Create an alias and reaload the source file: 

```
echo alias modbus="'/home/eneltec/industrial/.venv/bin/python3 /home/eneltec/industrial/modbus.py'" | sudo tee -a ~/.bashrc
source ~/.bashrc
```

4. Test the Modbus Interface:

``` 
modbus read coil 1 1 1
```