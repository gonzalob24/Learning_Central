# I could not import sound from pymixer
# I will spend a little more time on it a little later

from gpiozero import Button
import pygame.mixer
from pygame.mixer import sound
from signal import pause

pygame.mixer.init()

button_sounds = {
    Button(2) : sound("samples/drum_tom_mid_hard.wav"),
    Button(27) : sound("samples/drum/cymbal_open.wav")
}


for button, sound in button_sounds.item():
    button.when_pressed = sound.play

pause()
