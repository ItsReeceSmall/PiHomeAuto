import sys, os, time
import RPi.GPIO as gpio

class Board:
    def __init__(self):
        self.board = gpio
        self.setup()
    
    def setup(self):
        #self.cleanup()
        #print ('Warnings = False')
        self.board.setwarnings(False)
        #print ('Board = gpio.BOARD')
        self.board.setmode(self.board.BOARD)
    
    def cleanup(self):
        self.board.cleanup()

if __name__ == "__main__":
    b = Board()
