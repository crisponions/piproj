import time
import sys
from nintendo_font import NintendoFont as nf

s = nf('hello')
#def print_letter(f):
#    for i in f:
#        s.test_letter(i)

if __name__ == '__main__':
    for j in sys.argv[1]:
        s.print_letter(j)

