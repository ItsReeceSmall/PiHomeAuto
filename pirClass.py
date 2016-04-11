import RPi.GPIO as gpio
import time, os, sys

class Pir:
    def __init__(self, pirSensor):
        self.pirSensor = pirSensor
        self.pirState = 0
        self.pirMethod()
    
    def pirMethod(self):
        self.pirState = gpio.input(self.pirSensor)
        if self.pirState == 1:
            pirVal = 'on'
        elif self.pirState == 0:
            pirVal = 'off'
        else:
            print('Error PIR not functioning, aborting...')
            gpio.cleanup()
            sys.exit()

if __name__ == "__main__":
    p = Pir(pirSensor)
