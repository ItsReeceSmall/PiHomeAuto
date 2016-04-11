import RPi.GPIO as gpio
import time, os, sys

class Pir:
    def __init__(self, pirSensor):
        self.pirSensor = pirSensor
        self.pirMethod()
    
    def pirMethod(self):
        pirState = gpio.input(self.pirSensor)
        if pirState == 1:
            pirVal = 'on'
        elif pirState == 0:
            pirVal = 'off'
        else:
            print('Error PIR not functioning, aborting...')
            gpio.cleanup()
            sys.exit()

if __name__ == "__main__":
    p = Pir()
