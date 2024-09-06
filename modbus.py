#!/home/eneltec/.industrial/.venv/bin/python3

import argparse
from pymodbus.client import ModbusSerialClient
import socket

class FastModbus:
    def __init__(self):
        tty = '/dev/ttyS3' if socket.gethostname() == 'bananapim2zero' else '/dev/ttyS0'
        config = {'baudrate': 9600, 'stopbits': 1, 'bytesize': 8, 'parity': 'N', 'timeout': 3}
        self.client = ModbusSerialClient(port=tty, **config)
        self.client.connect()

    def read(self, slave, reg_type, reg, count):
        read_func = {'input': self.client.read_input_registers, 
                     'holding': self.client.read_holding_registers, 
                     'coil': self.client.read_coils, 
                     'discrete': self.client.read_discrete_inputs}
        return read_func[reg_type](reg, count, slave)

    def write(self, slave, reg_type, reg, values):
        write_func = {'holding': self.client.write_registers, 
                      'coil': self.client.write_coils}
        return write_func[reg_type](reg, values, slave)

def main():
    parser = argparse.ArgumentParser(description="Modbus Read/Write Script")
    parser.add_argument('operation', choices=['read', 'write'], help="Specify 'read' or 'write' operation")
    parser.add_argument('reg_type', choices=['coil', 'input', 'holding', 'discrete'], help="Register type")
    parser.add_argument('slave', type=int, help="Slave ID")
    parser.add_argument('reg', type=int, help="First register address")
    parser.add_argument('count', type=int, nargs='?', default=1, help="Number of registers (read) or values (write)")
    parser.add_argument('values', type=int, nargs='*', help="Values to write (only for write operation)")

    args = parser.parse_args()
    modbus = FastModbus()
    print(f"Operation: {args.operation}, Register Type: {args.reg_type}, Slave: {args.slave}, Register: {args.reg}, Count: {args.count}, Values: {args.values}")

    if args.operation == 'read':
        response = modbus.read(args.slave, args.reg_type, args.reg, args.count)
    elif args.operation == 'write':
        if not args.values:
            print("Please provide values to write.")
            return
        response = modbus.write(args.slave, args.reg_type, args.reg, args.values)

    if response.isError():
        print(f"Error: {response}")
    else:
        print(f"Response: {getattr(response, 'registers', 'Success')}")

if __name__ == "__main__":
    main()
