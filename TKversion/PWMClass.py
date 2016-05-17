class PWM:
    def __init__(self, ledPin, board, pwmval):
        self.board = board
        self.__ledPin = ledPin
        self.pwmval = int(pwmval)
        self.i = self.board.PWM(self.__ledPin, 100)
        self.i.start(0)

    def PWMLED(self):
        self.i.ChangeDutyCycle(self.pwmval)


import time, sys, os
from board import Board

board = Board().board

if __name__ == "__main__":
    board.setmode(board.BOARD)
    lightPin = input('Enter Pin: ')
    board.setup(lightPin, board.OUT)
    Led(lightPin, board, 0).LedOn()
    print('on')
    time.sleep(2)
    Led(lightPin, board, 0).LedOff()
    print('off')
    board.cleanup()