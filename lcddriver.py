import i2c_lib
import time

ADDRESS = 0x27  # Update to your device's I2C address

LCD_CHR = 1  # Mode - Sending data
LCD_CMD = 0  # Mode - Sending command
LCD_BACKLIGHT = 0x08  # On

LCD_CLEAR_DISPLAY = 0x01

class lcd:
    def __init__(self):
        self.lcd_device = i2c_lib.i2c_device(ADDRESS)
        self.lcd_write(0x03)
        self.lcd_write(0x03)
        self.lcd_write(0x03)
        self.lcd_write(0x02)

        self.lcd_write(0x28)
        self.lcd_write(0x0C)
        self.lcd_write(0x01)
        time.sleep(0.0005)

    def lcd_write(self, cmd, mode=LCD_CMD):
        self.lcd_write_four_bits(mode | (cmd & 0xF0))
        self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0))

    def lcd_write_four_bits(self, data):
        self.lcd_device.write_cmd(data | LCD_BACKLIGHT)
        self.lcd_strobe(data)

    def lcd_strobe(self, data):
        self.lcd_device.write_cmd(data | LCD_BACKLIGHT | 0x04)
        time.sleep(0.0005)
        self.lcd_device.write_cmd(data & ~0x04 | LCD_BACKLIGHT)
        time.sleep(0.0001)

    def lcd_display_string(self, string, line):
        if line == 1:
            self.lcd_write(0x80)
        elif line == 2:
            self.lcd_write(0xC0)
        for char in string:
            self.lcd_write(ord(char), LCD_CHR)

    def lcd_clear(self):
        self.lcd_write(LCD_CLEAR_DISPLAY)
        time.sleep(0.0005)
