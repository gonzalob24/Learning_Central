from gpiozero import Button
from signal import pause
from gpiozero import LED
from time import sleep
from gpiozero import PWMLED

button = Button(2)
led = LED(25)
button.wait_for_press()
led.blink()
sleep(1)

led.on()

sleep(2)
led.off()
