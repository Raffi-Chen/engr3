import rotaryio
import board
import neopixel
import digitalio
from lcd.lcd import LCD # importing lcd stuff below
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)

lcd = LCD(I2CPCF8574Interface(board.I2C(),0x27),num_rows=2,num_cols=16) 
# Begin communication with LCD screen
#i2c = busio.I2C(board.SCL,board.SDA)

led = neopixel.NeoPixel(board.NEOPIXEL,1)
led.brightness = 0.05
# Establishes properties of neopixel

button = digitalio.DigitalInOut(board.D2) # Establishes communication with 2nd pin
button.direction = digitalio.Direction.INPUT # Establishes button input
button.pull = digitalio.Pull.UP
button_state = 0

menu = ["stop         ", "caution         ", "go          "]

last_index = None
menu_index = 0

while True:

    menu_index = enc.position
    menu_index_lcd = menu_index % 3

    lcd.set_cursor_pos(0,0)
    lcd.print(menu[menu_index_lcd])

    if button.value and button_state == 0:
        print(f"Menu Index = {menu_index_lcd}")
        button_state = 1
        if menu_index_lcd is 0:

            led[0] = (255, 0, 0)

        if menu_index_lcd is 1:

            led[0] = (255, 255, 0)

        if menu_index_lcd is 2:

            led[0] = (0, 255, 0)

    elif not button.value:
        button_state = 0

#-------------------------------------

'''    led[0] = (255, 0, 0) # Projects certain color to LED

    if not button.value and button_state is None: # If button value is NOT 0 (if it is 1/pressed)
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button is pressed")
        button_state = None

    print(menu[menu_index_lcd])

    if (last_index is None) or (menu_index is not 0):
        #print(menu_index_lcd)
        last_index = menu_index

    time.sleep(1)'''