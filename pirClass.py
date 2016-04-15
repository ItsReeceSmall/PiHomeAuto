import RPi.GPIO as gpio
import time

class Pir:
    def __init__(self, pirSensor, board):
        self.time = time
        self.board = board
        self.pirSensor = pirSensor
        self.pirState = 0
        self.pirMethod()
    
    def pirMethod(self):
        for i in range(1, 13):
            self.pirState = self.board.input(self.pirSensor)
            value = self.board.input(self.pirSensor)
            time.sleep(0.3)
            print (self.pirState)
            print (value)
            if self.pirState == 1:
                self.pirState = 1
            elif self.pirState == 0:
                self.pirState = 0
            else:
                print('Error PIR not functioning, aborting...')
                self.board.cleanup()
                #sys.exit()
        return self.pirState

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    pirSensor = 32
    gpio.setup(pirSensor, gpio.IN)
    #p = Pir()
    for i in range(20):
        #p = Pir(pirSensor)
        pirState = gpio.input(pirSensor)
        print (pirState)
        time.sleep(0.3)
