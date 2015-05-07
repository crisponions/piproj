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
         
        self.letter_dict = {
                         'a': ['1c', '36', '63', '63', '7f', '63', '63'],
                         'b': ['3f', '63', '63', '3f', '63', '63', '3f'],
                         'c': ['3c', '66', '03', '03', '03', '66', '3c'],
                         'd': ['3f', '33', '63', '63', '63', '33', '3f'],
                         'e': ['7f', '03', '03', '3f', '03', '03', '7f'],
                         'f': ['7f', '03', '03', '3f', '03', '03', '03'],
                         'g': ['1f', '30', '60', '67', '63', '33', '1f'],
                         'h': ['63', '63', '63', '7f', '63', '63', '63'], 
                         'i': ['7e', '18', '18' ,'18' ,'18', '18', '7e'],
                         'j': ['78', '60', '60', '60', '63', '63', '3e'],
                         'k': ['63', '33', '1b', '07', '0f', '3b', '73'],
                         'l': ['03', '03', '03', '03', '03', '03', '7f'],
                         'm': ['63', '77', '7f', '7f', '6b', '63', '63'],
                         'n': ['63', '67', '6f', '7f', '7b' ,'73', '63'],
                         'o': ['3e', '63', '63', '63', '63', '63', '3e'],
                         'p': ['3f', '63', '63', '63', '3f', '03', '03'],
                         'q': ['3e', '63', '63', '63', '7b', '33', '5e'],
                         'r': ['3f', '63', '63', '73', '1f', '3b', '73'],
                         's': ['3e', '63', '03', '3e', '60', '63', '3e'],
                         't': ['7e', '18', '18' ,'18' ,'18', '18', '18'],
                         'u': ['63', '63', '63' ,'63', '63', '63', '3e'],
                         'v': ['63', '63', '63', '77', '3e', '1c' ,'08'],
                         'w': ['63', '63', '6b', '7f', '7f', '77', '63'],
                         'x': ['63', '77', '3e', '1c', '3e', '77', '63'],
                         'y': ['66', '66' ,'66', '3c' ,'18', '18', '18'],
                         'z': ['7f', '70', '38', '1c', '0e', '07', '7f'],  
                         'space': ['00']
                     }
    def test_letter(self, letter):
        
        letter_array = self.letter_dict[letter]
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

    def print_letter(self, letter):
        if letter == ' ':
            letter = 'space'
        for i in range(0,len(self.letter_dict[letter])):
            matrix.WriteRowRaw(i, self.letter_dict[letter])

