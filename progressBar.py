import RPi.GPIO as gpio
import time, os, sys, glob
from lcd1602 import LCD1602

lcd = LCD1602()

class Bar:
    def __init__(self):
        self.barMethod()
    
    def barMethod(self):
        la = [-1, 6.25, 12.5, 18.75, 25, 31.25, 37.5, 43.75, 50, 56.25, 62.5, 68.75, 75, 81.25, 87.5, 93.75, 100]
        ha = [6.25, 12.5, 18.75, 25, 31.25, 37.5, 43.75, 50, 56.25, 62.5, 68.75, 75, 81.25, 87.5, 93.75, 100, 106.25]
        val = -1
        state = 0
        low = la[state]
        high = ha[state]
        string = '/'
        debug = 1
        print('### DEBUG ###')
        for i in range(1, 102):
            print('### RUN ' + str(debug) + ' ###')
            debug = (debug + 1)
            print ('Low = ' + str(low) + ' / High = ' + str(high))
            print ('State = ' +   str(state) + ' / String = "' + string + '"')
            val = (val + 1)
            if val >= low and val <= high:
                lcd.lcd_string(string, lcd.LCD_LINE_1)
            else:
                string = (string + '/')
                state = (state + 1)
                low = la[state]
                high = ha[state]
            lcd.lcd_string('PROGRESS    ' + str(val) + '%', lcd.LCD_LINE_2)
            time.sleep(0.06)
        for i in range(1, 4):
            lcd.lcd_string('Process Complete', lcd.LCD_LINE_1)
            lcd.lcd_string('Opening Program.', lcd.LCD_LINE_2)
            time.sleep(0.8)
            lcd.lcd_clear()
            

if __name__ == "__main__":
    Bar()
    sys.exit()
