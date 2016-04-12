import RPi.GPIO as gpio
import time, os, sys, glob
from lcd1602 import LCD1602

lcd = LCD1602()

class Bar:
    def __init__(self):
        self.barMethod()
    
    def barMethod(self):
        # low range
        la = [-1, 6.25, 12.5, 18.75, 25, 31.25, 37.5, 43.75, 50, 56.25, 62.5, 68.75, 75, 81.25, 87.5, 93.75, 100]
        # high range
        ha = [6.25, 12.5, 18.75, 25, 31.25, 37.5, 43.75, 50, 56.25, 62.5, 68.75, 75, 81.25, 87.5, 93.75, 100, 106.25]
        val = -1            # value which shows on the screen as a percentage value
        state = 0           # State is the currently selected index for both la and ha
        low = la[state]     # sets low as the index value pulled from la according to the number set in state
        high = ha[state]    # sets high as the index value pulled from ha according to the number set in state
        string = '/'        # Initial set string
        debug = 1           # For debugging purposes it is used as a counter for how many times the loop runs.
        print('### DEBUG ###')
        for i in range(1, 102):
            print('### RUN ' + str(debug) + ' ###')
            debug = (debug + 1)
            print ('Low = ' + str(low) + ' / High = ' + str(high))
            print ('State = ' +   str(state) + ' / String = "' + string + '"')
            val = (val + 1)
            if val >= low and val <= high:
                lcd.lcd_string(string, lcd.LCD_LINE_1)  # prints the par according to percentage.
            else:
                string = (string + '/')
                state = (state + 1)     # as percent val is higher than range specified it raises to next range in array
                low = la[state]         # resets the values of low and high to there new vaues
                high = ha[state]
            lcd.lcd_string('PROGRESS    ' + str(val) + '%', lcd.LCD_LINE_2)
            time.sleep(0.06)
        for i in range(1, 4):
            lcd.lcd_string('Process Complete', lcd.LCD_LINE_1)
            lcd.lcd_string('Opening Program.', lcd.LCD_LINE_2)
            time.sleep(1)
            lcd.lcd_clear()
            time.sleep(1)
            

if __name__ == "__main__":
    Bar()
    sys.exit()
