import sys, os, time
import RPi.GPIO

class Board:
    def __init__(self):
        self.board = RPi.GPIO
        self.setup()
    
    def setup(self):
        self.board.GPIO.setwarnings(False)
        self.board.GPIO.setmode(self.GPIO.board, self.board.GPIO.BOARD)
