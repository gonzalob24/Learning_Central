from gpiozero import Button, LED
from time import sleep
import random

# create and LED object
led = LED(17)

player_1 = Button(2)
player_2 = Button(3)
quit_game = Button(27)

flag = True
if input("Ready to play: ") == "y":
    flag = True
else:
    flag = False

time = random.uniform(5, 10)
sleep(time)
led.on()

points_p1 = 0
points_p2 = 0

while flag:
    if player_1.is_pressed:
        points_p1 += 1
        print("Player 1 wins! has ", points_p1, " points")
        led.off()
        time = random.uniform(5, 10)
        sleep(time)
        led.on()

    if player_2.is_pressed:
        points_p2 += 1
        print("Player 2 wins! has ", points_p2, " points")
        led.off()
        time = random.uniform(5, 10)
        sleep(time)
        led.on()

    if quit_game.is_pressed:
        break

led.off()





