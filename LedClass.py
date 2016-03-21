import RPi.GPIO as gpio
import time, sys, os
import board

class Led:
    def __init__(self, powerLed):
        self.__powerLed = powerLed
        #self.powerLedOn()
        #self.powerLedOff()
        self.powerLedTest()
        
    @property
    def powerLed(self):
        return self.__powerLed
    
    @powerLed.setter
    def powerLed(self, value):
        self.__powerLed = value
    
    # Need to write code to setup all the pins that have been passed in
    
    def powerLedOn(self):
        gpio.output(self.__powerLed, gpio.HIGH)
        time.sleep(0.2)
    
    def powerLedOff(self):
        gpio.output(self.__powerLed, gpio.LOW)
        time.sleep(0.2)
    
    def powerLedTest(self):
        gpio.output(self.__powerLed, gpio.HIGH)
        time.sleep(2)
        gpio.output(self.__powerLed, gpio.LOW)
