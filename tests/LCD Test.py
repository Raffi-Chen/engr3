import time
import board
import adafruit_character_lcd.character_lcd_i2c as character_lcd

i2c = board.I2C()  # uses board.SCL and board.SDA
lcd = character_lcd.Character_LCD_I2C(i2c, 16, 2)

lcd.message = "Hello, world!"
time.sleep(5)
lcd.clear()