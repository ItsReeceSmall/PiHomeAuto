#from board import Board
import time, os, sys
#from lcd1602 import LCD1602

#board = Board().board
#lcd = LCD1602(board)

class Pins:
    def __init__(self, inputs, outputs, buttons, board, time):
        self.board = board
        self.time = time
        self.__buttons = buttons
        self.__inputs = inputs
        self.__outputs = outputs
        self.printPins()

    # Need to write code to setup all the pins that have been passed in
    
    def printPins(self):
        for pin in self.__inputs:
            self.board.setup(pin, self.board.IN)
            print ('### Pin ' + str(pin) + ' is setup as input')
            sys.stdout.write("\033[F")
            #lcd.lcd_string('Pin ' + str(pin) + ' setup', lcd.LCD_LINE_1)
            self.time.sleep(0.1)
        for pin in self.__outputs:
            self.board.setup(pin, self.board.OUT)
            print ('### Pin ' + str(pin) + ' is setup as output')
            sys.stdout.write("\033[F")
            #lcd.lcd_string('Pin ' + str(pin) + ' setup', lcd.LCD_LINE_1)
            self.time.sleep(0.1)
        for pin in self.__buttons:
            self.board.setup(pin, self.board.IN, pull_up_down=self.board.PUD_UP)
            print('### Button Pin ' + str(pin) + ' is setup as input')
            sys.stdout.write("\033[F")
            # lcd.lcd_string('Pin ' + str(pin) + ' setup', lcd.LCD_LINE_1)
            self.time.sleep(0.1)
        print('###########################################')
