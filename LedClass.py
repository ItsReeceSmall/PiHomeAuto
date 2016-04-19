class Led:
    def __init__(self, ledPin, board):
        self.board = board
        self.__ledPin = ledPin
    
    def LedOn(self):
        self.board.output(self.__ledPin, self.board.HIGH)
        time.sleep(0.1)
    
    def LedOff(self):
        self.board.output(self.__ledPin, self.board.LOW)
        time.sleep(0.1)
    
    def LedTest(self):
        self.board.output(self.__ledPin, self.board.HIGH)
        time.sleep(2)
        self.board.output(self.__ledPin, self.board.LOW)

import time, sys, os
from board import Board

board = Board().board

if __name__ == "__main__":
    board.setmode(board.BOARD)
    lightPin = input('Enter Pin: ')
    board.setup(lightPin, board.OUT)
    Led(lightPin, board).LedOn()
    print('on')
    time.sleep(2)
    Led(lightPin, board).LedOff()
    print('off')
    board.cleanup()