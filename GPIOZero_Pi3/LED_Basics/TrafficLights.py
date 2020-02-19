# Simulating a full traffic lights system

from gpiozero import TrafficLights
from time import sleep

# Create a lights object
lights = TrafficLights(5, 6, 13)

lights.green.on()

while True:
    sleep(10)
    lights.green.off()
    lights.amber.on()  # amber allows to switch lights continuously
    sleep(1)
    lights.amber.off()
    lights.red.on()
    sleep(10)
    lights.amber.on()
    sleep(1)
    lights.green.on()
    lights.amber.off()

    # or use
    # yield (0, 0, 1)
    # sleep(10)
    # yield (0, 1, 0) amber
    # sleep(1)
    # yield (1, 0, 0)
    # sleep(10)
    # yield (1, 0, 0) amber then green
    # sleep(1)



