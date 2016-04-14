import RPi.GPIO as gpio
from board import Board
import time, os, sys

class Pir:
    def __init__(self, pirSensor, board):
        self.board = board
        self.pirSensor = pirSensor
        self.pirState = 0
        self.pirMethod()
    
    def pirMethod(self):
        self.pirState = self.board.input(self.pirSensor)
        if self.pirState == 1:
            self.pirState = 1
        elif self.pirState == 0:
            self.pirState = 0
        else:
            print('Error PIR not functioning, aborting...')
            self.board.cleanup()
            sys.exit()

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    pirSensor = 32
    gpio.setup(pirSensor, gpio.IN)
    #p = Pir()
    for i in range(50):
        #p = Pir(pirSensor)
        pirState = gpio.input(pirSensor)
        print (pirState)
        time.sleep(0.1)
