import turtle


fname = open("labdata.txt", 'r')


def draw_dots():
    for line in fname:
        temp = line.split()
        x = int(temp[0])
        y = int(temp[1])
        tess.penup()
        tess.goto(x, y)
        tess.pendown()
        tess.stamp()
        

window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shapesize(.2, .2, .2)
tess.speed(1)
tess.shape("circle")

draw_dots()

window.exitonclick()
