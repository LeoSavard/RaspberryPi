from sense_hat import SenseHat
import time
sense = SenseHat()
temp = sense.get_temperature()

#colours
purple=(216, 155, 240)
red=(255, 0, 0)

sense.clear()
temperature = str(round(temp))
sense.show_message(temperature, text_colour=purple)
