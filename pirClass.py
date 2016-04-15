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
        for i in range(1, 13):
            time.sleep(0.4)
            self.pirState = self.board.input(self.pirSensor)
            print (self.pirState)
            if self.pirState == 1:
                self.pirState = 1
                break
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
        time.sleep(0.08)
