import sys
import RPi.GPIO as gpio

class Board:
    def __init__(self):
        self.board = gpio
        self.setup()
    
    def setup(self):
        self.board.setwarnings(False)
        self.board.setmode(self.board.BOARD)
    
    def cleanup(self):
        print('### User input recieved ###\n### Closing down ###')
        self.board.cleanup()
        sys.exit()

if __name__ == "__main__":
    b = Board()
