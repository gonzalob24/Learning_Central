from gpiozero import Button
from gpiozero import LED

button = Button(2)
led = LED(25)

# you can also place this in a while
while True:
    button.when_pressed = led.on
    button.when_pressed = led.off
    
# or use led.source = button to implement the below code
button.when_pressed = led.on
button.when_released = led.off


def say_hi():
    print("Hey hi")


def say_bye():
    print("Bye")
    
# the function does not run the function say_hi
# it creates a reference to the function to be called
# when the button is pressed
# button.when_pressed = say_hi
# button.when_released = say_bye

# print("Button was pressed")
# 
# while True:
#     if button.is_pressed:  # returns boolean
#         print("Button was pressed")
#     else:
#         print("Button was not pressed after 2 seconds")
#         print("Finished")
