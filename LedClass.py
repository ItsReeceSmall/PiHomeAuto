class Led:
    def __init__(self, ledPin, board, brightness):
        self.board = board
        self.__ledPin = ledPin
        self.brightness = brightness

    
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

    def PWMLED(self):
        self.board.PWM(self.__ledPin, 100).start(0).ChangeDutyCycle(self.brightness)

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