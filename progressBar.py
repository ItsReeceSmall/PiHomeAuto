import RPi.GPIO as gpio
import time, os, sys, glob
from lcd1602 import LCD1602

lcd = LCD1602()

class Bar:
    def __init__(self):
        self.barMethod()
    
    def barMethod(self):
        val = -1
        #mult = 0
        for i in range(1, 102):
            val = (val + 1)
            #mult = (mult + 0.0618811881188119)
            if val > 6.25:
                lcd.lcd_string('█', lcd.LCD_LINE_1)
                if val > 12.5:
                    lcd.lcd_string('██', lcd.LCD_LINE_1)
                    if val > 18.75:
                        lcd.lcd_string('███', lcd.LCD_LINE_1)
                        if val >= 25:
                            lcd.lcd_string('████', lcd.LCD_LINE_1)
                            if val > 31.25:
                                lcd.lcd_string('█████', lcd.LCD_LINE_1)
                                if val > 37.5:
                                    lcd.lcd_string('██████', lcd.LCD_LINE_1)
            lcd.lcd_string('PROGRESS    ' + str(val) + '%', lcd.LCD_LINE_2)
            time.sleep(0.06)
            

if __name__ == "__main__":
    Bar()
    sys.exit()
