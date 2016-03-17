import RPi.GPIO as gpio
import time, os, sys

class Pins:
    def __init__(self, inputs, outputs):
        self.__inputs = inputs
        self.__outputs = outputs
        self.printPins()
        
    @property
    def Inputs(self):
        return self.__inputs
    
    @Inputs.setter
    def Inputs(self, value):
        self.__inputs = value
        
    @property
    def Outputs(self):
        return self.__outputs
        
    @Outputs.setter
    def Outputs(self, value):
        self.__outputs = value
    
    # Need to write code to setup all the pins that have been passed in
    
    def printPins(self):
        for pin in self.__inputs:
            gpio.setup(pin, gpio.IN)
            print ('### Pin ' + str(pin) + ' is setup')
        for pin in self.__outputs:
            gpio.setup(pin, gpio.OUT)
            print ('### Pin ' + str(pin) + ' is setup')
