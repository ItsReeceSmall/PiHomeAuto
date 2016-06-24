import sys
import RPi.GPIO as gpio

class Board:
    def __init__(self):
        self.board = gpio
        self.setup()
        # sets up board
    
    def setup(self):
        self.board.setwarnings(False)
        self.board.setmode(self.board.BOARD)
        # sets up what mode the board is
    
    def cleanup(self):
        print('### User input recieved ###\n### Closing down ###')
        self.board.cleanup()
        sys.exit()
        # cleanup method to end the program safely

if __name__ == "__main__":
    b = Board()
