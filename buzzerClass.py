import RPi.GPIO as gpio
import time
from board import Board
board = Board().board

class Buzz:
    def __init__(self, buzzSensor, board):
        self.board = board
        self.buzzSensor = 35
        self.outpin()

    def outpin(self):
        self.board.setup(self.buzzSensor, self.board.OUT)

    def buzzOn(self):
        self.board.output(self.buzzSensor, self.board.HIGH)
        #print ('buzzer on')# Buzzer On

    def buzzOff(self):
        self.board.output(self.buzzSensor, self.board.LOW)
        #print('buzzer off')  # Buzzer Off

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    buzzSensor = 35
    gpio.setup(buzzSensor, gpio.OUT)
    b = Buzz(buzzSensor, board)
    #b.buzzMethod()