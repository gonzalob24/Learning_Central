import turtle
turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

tess2 = turtle.Turtle()
tess2.color("red")
tess2.pensize(3)
tess2.shape("circle")


def h1(x, y):
    wn.title("Got click at coords {0}, {1}".format(x, y))
    tess.goto(x, y)

def h2(x, y):
    wn.title("Got click at coords {0}, {1}".format(x, y))
    tess2.goto(x, y)

tess.onclick(h1)  # Wire up a click on the window.
tess2.onclick(h2)
wn.mainloop()
