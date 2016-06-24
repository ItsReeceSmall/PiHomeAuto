class Led:
    def __init__(self, ledPin, board, pwmval):
        self.board = board
        self.__ledPin = ledPin
        self.pwmval = int(pwmval)

    def LedOn(self):
        self.board.output(self.__ledPin, self.board.HIGH)
        time.sleep(0.1)
        # Turns LED on
    
    def LedOff(self):
        self.board.output(self.__ledPin, self.board.LOW)
        time.sleep(0.1)
        # Turns LED off
    
    def LedTest(self):
        self.board.output(self.__ledPin, self.board.HIGH)
        time.sleep(2)
        self.board.output(self.__ledPin, self.board.LOW)
        # Turns LED on and off to test it works.

    def PWMLED(self):
        i = self.board.PWM(self.__ledPin, 100)
        i.start(0)
        time.sleep(0.1)
        i.ChangeDutyCycle(self.pwmval)
        # Parses in pin and starts it, then changes the output of the power through the pwmval.

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
