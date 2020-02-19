import turtle
turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Using a timer to get events!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("purple")


def h1():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h1, 2000)        #sets the speed of the timer


h1()
wn.mainloop()
