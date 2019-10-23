from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (3280, 2464)
camera.start_preview()
for i in range(1):
    sleep(5)
    camera.capture('/media/pi/Samsung USB/Pictures/PiCamera/image%s.jpg' % i)
camera.stop_preview()