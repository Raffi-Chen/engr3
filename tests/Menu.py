import rotaryio
import board
import time

menu = ["stop", "caution", "go"]

last_index = None
menu_index = 0



enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)

while True:

    menu_index = enc.position
    menu_index_lcd = menu_index % 3
    print(menu[menu_index_lcd])

    if (last_index is None) or (menu_index is not 0):
        #print(menu_index_lcd)
        last_index = menu_index

    time.sleep(1)