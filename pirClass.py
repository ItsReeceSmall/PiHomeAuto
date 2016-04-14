import RPi.GPIO as gpio
import time, os, sys

####    PIR PHYSICALLY NOT WORKING ####

class Pir:
    def __init__(self, pirSensor):
        self.pirSensor = pirSensor
        self.pirState = 0
        self.pirMethod()
    
    def pirMethod(self):
        self.pirState = gpio.input(self.pirSensor)
        if self.pirState == 1:
            self.pirState = 1
        elif self.pirState == 0:
            self.pirState = 0
        else:
            print('Error PIR not functioning, aborting...')
            gpio.cleanup()
            sys.exit()

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    pirSensor = 32
    gpio.setup(pirSensor, gpio.IN)
    #p = Pir()
    for i in range(50):
        p = Pir(pirSensor)
        pirState = p.pirMethod()
        print (pirState)
        time.sleep(0.1)
