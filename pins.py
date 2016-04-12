import RPi.GPIO as gpio
import time, os, sys
from lcd1602 import LCD1602

lcd = LCD1602()

class Pins:
    def __init__(self, inputs, outputs):
        self.__inputs = inputs
        self.__outputs = outputs
        self.printPins()

    # Need to write code to setup all the pins that have been passed in
    
    def printPins(self):
        for pin in self.__inputs:
            gpio.setup(pin, gpio.IN)
            lcd.lcd_string('Pin ' + pin + ' setup', lcd.LCD_LINE_1)
            print ('### Pin ' + str(pin) + ' is setup')
            time.sleep(0.15)
        for pin in self.__outputs:
            gpio.setup(pin, gpio.OUT)
            lcd.lcd_string('Pin ' + pin + ' setup', lcd.LCD_LINE_1)
            print ('### Pin ' + str(pin) + ' is setup')
            time.sleep(0.15)
