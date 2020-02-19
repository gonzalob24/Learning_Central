# For the button

from gpiozero import Button

# For the camera, first install PiCamera module if not installed
from picamera import PiCamera

# Creating a button object
button = Button(2)
camera = PiCamera()

camera.start_preview()
frame = 1

while True:
    button.wait_for_press()
    camera.capture('/home/pi/frame%03d.jpg' % frame)
    frame += 1
