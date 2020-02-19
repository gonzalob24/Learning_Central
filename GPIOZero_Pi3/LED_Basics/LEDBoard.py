from gpiozero import LEDBoard
from time import sleep
from signal import pause
from gpiozero import PWMLED

# Create my LEDs

leds = LEDBoard(5, 6, 13, 19, 26)
#leds = LEDBoard(5, 6, 13, 19, 26, pwm=True)
leds2 = PWMLED(5)  # Have to create each led individually to be used with pulse
leds.on()
sleep(1)
leds.off()
sleep(1)
leds.value(1, 0, 1, 0, 1)
sleep(1)
leds.blink()
sleep(3)
leds2.pulse(2, 1, 1, False)
