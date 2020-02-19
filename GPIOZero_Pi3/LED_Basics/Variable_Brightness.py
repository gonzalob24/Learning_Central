# PWM allows to change the brightness of LEDs
# values between 0 and 1

from gpiozero import LED
from gpiozero import PWMLED
from time import sleep

led = PWMLED(25)
flag = True
while(flag):
    led.value = 0
    sleep(1)
    led.value = 0.5
    sleep(1)
    led.value = 1
    sleep(1)
    led.off()
    flag = False

# led.pulse() has the same effect as above

print("Test Finished")
