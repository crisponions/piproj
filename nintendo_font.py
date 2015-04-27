#!/usr/bin/python
#
# Library to print Nintendo Characters
# On an adafruit 8x8 LEDBackpack.
#
class NintendoFont:

    '''
       NintendoFont-Class that draws letters
       using NES font on an Adafruit 8x8 LED matrix.
       grid is laid out from right to left
        0 1 2 3 4 5 6 7
      0 . . . . . . . .
      1 . . . . . . . .
      2 . . . . . . . .
      3 . . . . . . . .
      4 . . . . . . . .
      5 . . . . . . . .
      6 . . . . . . . .
      7 . . . . . . . .

      binary is a mirror image of grid. 
      00000011 (0x0003) will light
      pixels 0 and 1 .

      Nintendo Font uses a 7x7 grid
      the class utilizes pixels (0-6)x(0-6)
    '''


    def __init__(self, matrix):
        self.matrix = matrix
        
    def a(self):
        self.matrix.writeRowRaw(0,0x001C)
        self.matrix.writeRowRaw(1,0x0036)
        self.matrix.writeRowRaw(2,0x0063)
        self.matrix.writeRowRaw(3,0x0063)
        self.matrix.writeRowRaw(4,0x007F)
        self.matrix.writeRowRaw(5,0x0063)
        self.matrix.writeRowRaw(6,0x0063)
    def b(self):
        self.matrix.writeRowRaw(0,0x003f)
        self.matrix.writeRowRaw(1,0x0063)
        self.matrix.writeRowRaw(2,0x0063)
        self.matrix.writeRowRaw(3,0x003f)
        self.matrix.writeRowRaw(4,0x0063)
        self.matrix.writeRowRaw(5,0x0063)
        self.matrix.writeRowRaw(6,0x003f)
    def c(self):
        self.matrix.writeRowRaw(0,0x003c)
        self.matrix.writeRowRaw(1,0x0066)
        self.matrix.writeRowRaw(2,0x0003)
        self.matrix.writeRowRaw(3,0x0003)
        self.matrix.writeRowRaw(4,0x0003)
        self.matrix.writeRowRaw(5,0x0066)
        self.matrix.writeRowRaw(6,0x003c)
    def d(self):
        self.matrix.writeRowRaw(0,0x003f)
	self.matrix.writeRowRaw(1,0x0033)
        self.matrix.writeRowRaw(2,0x0063)
        self.matrix.writeRowRaw(3,0x0063)
        self.matrix.writeRowRaw(4,0x0063)
        self.matrix.writeRowRaw(5,0x0033)
        self.matrix.writeRowRaw(6,0x003f)

    def e(self):
        self.matrix.writeRowRaw(0,0x007f)
        self.matrix.writeRowRaw(1,0x0003)
        self.matrix.writeRowRaw(2,0x0003)
        self.matrix.writeRowRaw(3,0x003f)
        self.matrix.writeRowRaw(4,0x0003)
        self.matrix.writeRowRaw(5,0x0003)
        self.matrix.writeRowRaw(6,0x007f)

    def f(self):
        pass
    def g(self):
        self.matrix.writeRowRaw(0,0x001f)
        self.matrix.writeRowRaw(1,0x0030)
        self.matrix.writeRowRaw(2,0x0060)
        self.matrix.writeRowRaw(3,0x0067)
        self.matrix.writeRowRaw(4,0x0063)
        self.matrix.writeRowRaw(5,0x0033)
        self.matrix.writeRowRaw(6,0x001f)
    def h(self):
        pass
    def i(self):
        pass
    def j(self):
        pass
    def k(self):
        pass
    def l(self):
        self.matrix.writeRowRaw(0,0x0003)
        self.matrix.writeRowRaw(1,0x0003)
        self.matrix.writeRowRaw(2,0x0003)
        self.matrix.writeRowRaw(3,0x0003)
        self.matrix.writeRowRaw(4,0x0003)
        self.matrix.writeRowRaw(5,0x0003)
        self.matrix.writeRowRaw(6,0x007f)

    def m(self):
        pass
    def n(self):
        pass
    def o(self):
        self.matrix.writeRowRaw(0,0x003e)
        for num in range(1,6):
             self.matrix.writeRowRaw(num,0x0063)
        self.matrix.writeRowRaw(6,0x003e)
    def p(self):
        pass
    def q(self):
        pass
    def r(self):
        self.matrix.writeRowRaw(0,0x003f)
        self.matrix.writeRowRaw(1,0x0063)
        self.matrix.writeRowRaw(2,0x0063)
        self.matrix.writeRowRaw(3,0x0073)
        self.matrix.writeRowRaw(4,0x001f)
        self.matrix.writeRowRaw(5,0x003b)
        self.matrix.writeRowRaw(6,0x0073)
    def s(self):
        return ('0x003e', '0x0063', '0x0003', '0x003e', '0x0060', '0x0063', '0x003e')
        #self.matrix.writeRowRaw(0,0x003e)
        #self.matrix.writeRowRaw(1,0x0063)
        #self.matrix.writeRowRaw(2,0x0003)
        #self.matrix.writeRowRaw(3,0x003e)
        #self.matrix.writeRowRaw(4,0x0060)
        #self.matrix.writeRowRaw(5,0x0063)
        #self.matrix.writeRowRaw(6,0x003e)
    def t(self):
        pass
    def u(self):
        pass
    def v(self):
        pass
    def w(self):
        pass
    def x(self):
        pass
    def y(self):
        pass
    def z(self):
        pass
    
    def print_letter(self, letter):
        function_dict = {
                         'a': self.a,
                         'b': self.b,
                         'c': self.c,
                         'd': self.d,
                         'e': self.e,
                         'f': self.f,
                         'g': self.g,
                         'h': self.h,
                         'i': self.i,
                         'j': self.j,
                         'k': self.k,
                         'l': self.l,
                         'm': self.m,
                         'n': self.n,
                         'o': self.o,
                         'p': self.p,
                         'q': self.q,
                         'r': self.r,
                         's': self.s,
                         't': self.t,
                         'u': self.u,
                         'v': self.v,
                         'w': self.w,
                         'x': self.x,
                         'y': self.y,
                         'z': self.z,
                       }
        try:
            function = function_dict[letter]
            function()
            #eval(function)
        except KeyError:
            print 'Invalid Function'


    def test_letter(self, letter_array):
        
        def draw(bin_num):
            row = ''
            for num in bin_num:
                if num == '1':
                    row += '#'
                else:
                    row += ' '
            print row
         
        for item in letter_array:
            bin_num = self.hex_to_bin(item)
            while (len(bin_num) < 7):
                bin_num = '0' + bin_num
            draw(bin_num[::-1])
        
    def hex_to_bin(self, hex_num):
        try:
            return bin(int(hex_num,16))[2:]
        except:
            return Null
