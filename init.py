import RPi.GPIO as gpio
import time, os, sys
import pins

def setup():
    #set GPIO up
    gpio.setmode(gpio.BOARD)
    #gpio.setwarnings(False)
    #Set up pins from a class
    powerLed = 6
    tempSensor = 8
    # Set there categories
    inputs = [tempSensor]
    outputs = [powerLed]
    print('### ATTEMPTING TO IMPORT AND SETUP PINS ###')
    thepins = pins.Pins(inputs, outputs)
    print('### ALL PINS IMPORTED AND SETUP SUCCESSFULLY ###')

setup()
