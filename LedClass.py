import RPi.GPIO as gpio
import time, sys, os
from board import Board

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

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    lights = [37,11,13,15]
    for pin in lights:
        gpio.setup(pin, gpio.OUT)
        print (str(pin) + ' is set to out')
        gpio.output(pin, gpio.HIGH)
        time.sleep(0.2)
    time.sleep(3)
    for pin in lights:
        gpio.output(pin, gpio.LOW)
        time.sleep(0.2)
    gpio.cleanup()