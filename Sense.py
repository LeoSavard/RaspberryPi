from sense_hat import SenseHat
sense = SenseHat()
purple=(216, 155, 240)

sense.clear()

temp = sense.get_temperature()
print(temp)

from sense_hat import SenseHat
sense = SenseHat()
purple=(216, 155, 240)

sense.clear()
temp = sense.get_temperature()
display = sense.show_message()
while True:
  display(temp)