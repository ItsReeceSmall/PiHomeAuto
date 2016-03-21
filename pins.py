import RPi.GPIO as gpio
import time, os, sys
import board

class Pins:
    def __init__(self, inputs, outputs):
        self.__inputs = inputs
        self.__outputs = outputs
        self.printPins()

    # Need to write code to setup all the pins that have been passed in
    
    def printPins(self):
        for pin in self.__inputs:
            self.board.setup(pin, self.board.IN)
            print ('### Pin ' + str(pin) + ' is setup')
        for pin in self.__outputs:
            self.board.setup(pin, self.board.OUT)
            print ('### Pin ' + str(pin) + ' is setup')
