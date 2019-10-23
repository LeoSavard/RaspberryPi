##running from cli:python3.7 point-and-shoot.py
from sense_hat import SenseHat
from picamera import PiCamera
import time
from time import sleep
sense = SenseHat()
camera = PiCamera()
temp = round(sense.get_temperature())
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())
timestr = time.strftime("%Y%m%d-%H%M%S")

OFFSET_LEFT = 1
OFFSET_TOP = 2

NUMS =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
       0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
       1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
       1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
       1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
       1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
       1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
       1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
       1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
       1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9

# Displays a single digit (0-9)
def show_digit(val, xd, yd, r, g, b):
  offset = val * 15
  for p in range(offset, offset + 15):
    xt = p % 3
    yt = (p-offset) // 3
    sense.set_pixel(xt+xd, yt+yd, r*NUMS[p], g*NUMS[p], b*NUMS[p])

# Displays a two-digits positive number (0-99)
def show_number(val, r, g, b):
  abs_val = abs(val)
  tens = abs_val // 10
  units = abs_val % 10
  if (abs_val > 9): show_digit(tens, OFFSET_LEFT, OFFSET_TOP, r, g, b)
  show_digit(units, OFFSET_LEFT+4, OFFSET_TOP, r, g, b)


################################################################################
# MAIN
#colour definitions
w = (255, 255, 255)#white
pu=(216, 155, 240)#purple
p=(255, 0, 255)#pink
b=(0, 0, 0)#pink
y=(255, 255, 0)#yellow
pict_insta1=[
    b, b, b, b, b, p, b, b,
    b, p, p, p, p, p, p, b,
    b, p, b, b, b, b, p, b,
    b, p, b, p, p, b, p, b,
    b, p, b, p, p, b, p, b,
    b, p, b, b, b, b, p, b,
    b, p, p, p, p, p, p, b,
    b, b, b, b, b, b, b, b
]
pict_insta2=[
    b, b, b, b, b, y, b, b,
    b, p, p, p, p, p, p, b,
    b, p, b, b, b, b, p, b,
    b, p, b, p, p, b, p, b,
    b, p, b, p, p, b, p, b,
    b, p, b, b, b, b, p, b,
    b, p, p, p, p, p, p, b,
    b, b, b, b, b, b, b, b
    ]

sense.clear()
while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":

      # Check which direction
      if event.direction == "up": #Pressing up triggers a photo to be taken
        sense.set_pixels(pict_insta1)
        sleep(0.5)
        sense.clear()
        camera.start_preview()
        camera.resolution = (3280, 2464)
        for i in range(1):
            sleep(2)
            camera.capture('/media/pi/Samsung USB/Pictures/PiCamera/%s.jpg' % timestr)
        camera.stop_preview()
        sense.set_pixels(pict_insta2)
        sleep(0.5)
        sense.clear()
      elif event.direction == "down": #triggers a temperature probing
        event.direction =="down"
        show_number(temp, 200, 0, 60)
      elif event.direction == "left":
        sense.show_letter("L")      # Left arrow
      elif event.direction == "right":
        sense.show_letter("R")      # Right arrow
      elif event.direction == "middle":
        sense.show_letter("M")      # Enter key

      # Wait a while and then clear the screen
      sleep(0.5)
      sense.clear()
