import rotaryio
import board

menu = ["stop", "caution", "go"]

last_index = None
menu_index = 0

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)

while True:

    menu_index = enc.position

    if (last_index is None) or (menu_index is not 0):
        print(menu_index)
        last_index = menu_index