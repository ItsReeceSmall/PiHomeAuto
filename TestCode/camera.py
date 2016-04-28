import picamera, sys

cam = picamera.PiCamera()

try:
    cam.start_preview()
except KeyboardInterrupt:
    sys.exit()