import RPi.GPIO as gpio
import time, os, sys
import pins
import LedClass

def setup():
    gpio.setmode(gpio.BOARD)    #set GPIO up
    #gpio.setwarnings(False)
    powerLed = 6
    tempSensor = 8
    inputs = [tempSensor]   # Set there categories in arrays
    outputs = [powerLed]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    thepins = pins.Pins(inputs, outputs)    #Set up pins from a class
    print('### ALL PINS IMPORTED AND SETUP SUCCESSFULLY ###')

setup()
ledrun = LedClass.Led()
