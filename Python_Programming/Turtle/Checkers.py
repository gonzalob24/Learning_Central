# checkers its a perfect square
# squares on each row alternating colors


import turtle

turtle.setup(800, 800)
window = turtle.Screen()
window.title("Checkers")

pen = turtle.Turtle()
#pen.hideturtle()
#pen.shape("circle")
circ = pen.circle(40)  # creates a circle of radius 3
pen.ondrag(turtle.goto)

turtle.home()
turtle.begin_poly()
turtle.fd(100)
turtle.left(20)
turtle.fd(30)
turtle.left(60)
turtle.fd(50)
turtle.end_poly()
p = turtle.get_poly()

window.mainloop()
