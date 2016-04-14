import sys, os, time
import RPi.GPIO as gpio

class Board:
    def __init__(self):
        self.board = gpio
        self.setup()
    
    def setup(self):
        print ('Warnings = False')
        self.board.setwarnings(False)
        print ('Board = gpio.BOARD')
        self.board.setmode(self.board.BOARD)

if __name__ == "__main__":
    b = Board()
