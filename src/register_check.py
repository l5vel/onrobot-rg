from pymodbus.client.sync import ModbusTcpClient

# Update with your gripper's IP
client = ModbusTcpClient("192.168.0.27", port=502, timeout=3)
client.connect()

try:
    # Try reading 100 registers from address 0
    for itr in range(1000):
        result = client.read_holding_registers(address=itr, count=1, unit=65)
        
        if result is None or not hasattr(result, "registers") or result == 0:
            continue
        else:
            for i, val in enumerate(result.registers):
                if val != 0:
                    print(f"Register {itr}, {i}: {val}")

finally:
    client.close()