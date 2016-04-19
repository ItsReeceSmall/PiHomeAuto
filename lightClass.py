import RPi.GPIO as gpio
import time, sys, os
from board import Board

board = Board().board

class Light:
    def __init__(self, lightSensor, board):
        self.board = board
        self.lightSensor = lightSensor
        self.lightMehtod()

    def lightMethod(self):
        self.board.setup(lightSensor, self.board.OUT)
        self.board.output(lightSensor, self.board.LOW)
        measurement = 0
        time.sleep(0.05)
        self.board.setup(lightSensor,self.board.IN)
        #for i in range(1,11):
        if self.board.input(lightSensor) == self.board.LOW:
            measurement += 1
        return measurement

if __name__ == "__main__":
    l = Light()
    lightSensor = 18
    value = l.lightMethod(lightSensor, board)
    print (value)
