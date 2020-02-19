# Simulating a full traffic lights system

from gpiozero import TrafficLights
from time import sleep
from signal import pause


# Create a lights object
lights = TrafficLights(5, 6, 13)


# create a function
def traffic_lights():
    while True:
        yield (0, 0, 1)  # Green
        sleep(10)
        yield (0, 1, 0)  # amber
        sleep(1)
        yield (1, 0, 0)  # Red
        sleep(10)
        yield (1, 0, 0)  # Red+amber
        sleep(1)

pause()


if __name__ == '__main__':
    lights.source = traffic_lights()
