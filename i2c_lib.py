import smbus

class i2c_device:
    def __init__(self, addr, port=1):
        self.addr = addr
        self.bus = smbus.SMBus(port)

    def write_cmd(self, cmd):
        try:
            self.bus.write_byte(self.addr, cmd)
        except OSError as e:
            print(f"Error writing to I2C device at address {self.addr}: {e}")
            # Implement a retry mechanism if necessary
