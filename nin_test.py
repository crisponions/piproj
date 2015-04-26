import time
from nintendo_font import NintendoFont
from Adafruit_8x8 import EightByEight

grid = EightByEight(address=0x70)
matrix = NintendoFont(grid)
#matrix.print_letter('o')
for letter in 'oscar':
    matrix.print_letter(letter)
    time.sleep(1)
grid.clear()

