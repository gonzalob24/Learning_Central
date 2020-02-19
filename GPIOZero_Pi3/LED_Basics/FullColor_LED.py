from gpiozero import Button
from gpiozero import RGBLED
from time import sleep

# Create LED object
led = RGBLED(red=9, green=10, blue=11)
led.red = 1
sleep(1)

led.red = 0.5
sleep(1)

led.color = (0, 1, 0)  # Full green
sleep(1)

led.color = (1, 0, 1)  # Full magenta
sleep(1)

led.color = (1, 1, 0)  # Yellow
sleep(1)

led.color = (0, 1, 1)  # Cyan
sleep(1)

led.color = (1, 1, 1)  # white
sleep(1)

led.color = (0, 0, 0)  # Off
sleep(1)

# We can slowly increase the intensity of the blue color
for n in range(100):
    led.blue = n/100
    sleep(0.1)


