import RPi.GPIO as gpio
import time, os, sys

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 32
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
               print (“Motion Detected!”)

print (“PIR Module Test (CTRL+C to exit)”)
time.sleep(2)
print (“Ready”)

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                              time.sleep(100)
except KeyboardInterrupt:
               print (“ Quit”)
               GPIO.cleanup()

