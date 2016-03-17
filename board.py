import sys, os, time
import RPi.GPIO

class Board:
    def __init__(self):
        self.board = RPi.GPIO
    
    def setup(self):
        self.board.setwarnings(False)
        self.board.setmode(self.board, self.board.BOARD)
