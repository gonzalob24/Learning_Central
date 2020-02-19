import turtle


def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("      " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()


window = turtle.Screen()  # sets up the window
window.bgcolor("lightblue")  # changes the color of the window

tess = turtle.Turtle()  # creates the turtle
tess.color("blue", "red")
tess.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]

for number in xs:
    draw_bar(tess, number)

window.mainloop()
