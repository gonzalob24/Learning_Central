# This import needs to be first
from __future__ import division  # required for python 2 import
from gpiozero import LEDBarGraph
from time import sleep

# Create a graph object
graph = LEDBarGraph(5, 6, 13, 19, 26, 21)
# graph = LEDBarGraph(5, 6, 13, 19, 26, 21, pwm=True)
# Allows for more precise values for LED's
graph.value = 1      # (1, 1, 1, 1, 1, 1) all are ones or on
sleep(1)
graph.value = 1/2    # (1, 1, 1, 0, 0, 0)
sleep(1)
graph.value = -1/2   # ( 0, 0, 0, 1, 1, 1)
sleep(1)
graph.value = 1/4    # (1, 0, 0, 0, 0, 0)
sleep(1)
graph.value = -1     # (1, 1, 1, 1, 1, 1) all are ones or LEDs are on
