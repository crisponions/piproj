import time
import sys
from nintendo_font import NintendoFont as nf

s = nf('hello')
def print_letter(f):
    for i in f:
        s.test_letter(i)

if __name__ == '__main__':
    print_letter(sys.argv[1])

