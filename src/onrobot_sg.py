#!/usr/bin/env python3

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import time

class SG():
    def __init__(self, ip, port):
        self.client = ModbusClient(
            ip,
            port=port,
            stopbits=1,
            bytesize=8,
            parity='E',
            baudrate=115200,
            timeout=1)
        self.open_connection()

    def open_connection(self):
        """Opens the connection with a gripper."""
        self.client.connect()

    def close_connection(self):
        """Closes the connection with the gripper."""
        self.client.close()

    def set_target(self, command):
        """
        Min = 11mm
        Max = 75mm
        """
        if command < 110:
            command = 110
        elif command > 750:
            command = 750

        self.client.write_register(
            address=0, value=command, unit=65)  

    def set_init(self):
        self.client.write_register(
            address=1, value=0x3, unit=65)  
        
    def set_move(self):
        self.client.write_register(
            address=1, value=0x1, unit=65)  
        
    def set_gentle(self, command):
        """
        True or False

        If true, the gripping speed is reduced at 12.5mm before the specified target
        width, resulting in a gentler grip compared to normal grip settings.
        """
        self.client.write_register(
            address=2, value=command, unit=65) 

    def set_model_id(self, type_id):
        self.client.write_register(
            address=3, value=type_id, unit=65)  # 0x0003 -> 3

    def get_gp_wd(self):
        result = self.client.read_holding_registers(
            address=256, count=1, unit=65)  # 0x0100 -> 256
        return result.registers[0]

    def get_status(self):
        result = self.client.read_holding_registers(
            address=259, count=1, unit=65)  # 0x0103 -> 259
        return result.registers[0]

    def get_gp_max_wd(self):
        result = self.client.read_holding_registers(
            address=261, count=1, unit=65)  # 0x0105 -> 261
        return result.registers[0]

    def get_gp_min_wd(self):
        result = self.client.read_holding_registers(
            address=262, count=1, unit=65)  # 0x0106 -> 262
        return result.registers[0]
