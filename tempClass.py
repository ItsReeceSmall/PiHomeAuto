import os
import glob
import time
from lcd1602 import LCD1602

lcd = LCD1602()
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

class Temp:
    def __init__(self):
        pass

    def read_temp():
        lcd.lcd_string('Reading', lcd.LCD_LINE_1)
        lcd.lcd_string('     Temperature', lcd.LCD_LINE_2)
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f
    
if __name__ == "__main__":
    t = Temp()
    c, f = t.read_temp()
    val = str(int(c))
    print val
