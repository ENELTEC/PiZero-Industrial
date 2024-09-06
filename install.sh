echo dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=12 | sudo tee -a /boot/firmware/config.txt
echo dtoverlay=spi-bcm2835-overlay | sudo tee -a /boot/firmware/config.txt
sudo apt-get install can-utils
sudo ip link set can0 up type can bitrate 125000
sudo chmod +x .industrial/modbus.py
sudo python3 -m venv .industrial/.venv
sudo .industrial/.venv/bin/pip install pyserial==3.5
sudo .industrial/.venv/bin/pip install pymodbus==3.7.2
echo alias modbus="'/home/eneltec/.industrial/.venv/bin/python3 /home/eneltec/.industrial/modbus.py'" | sudo tee -a ~/.bashrc
source ~/.bashrc

echo "Installation complete. Please reboot the system."