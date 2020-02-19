# PWM allows to change the brightness of LEDs
# values between 0 and 1

from gpiozero import LED
from gpiozero import PWMLED
from time import sleep

led = PWMLED(25)
led.pulse(2, 1, 1, False)
