#program that will draw a five point star
"""
import turtle

window = turtle.Screen()
window.bgcolor("cyan") # Change color of screen
guy = turtle.Turtle() # Create yout turtle
guy.shape("turtle") # Change the shape
guy.pensize(5)
# guy.hideturtle()
guy.color("blue", "red")


def draw_star(size):
	for i in range(5):
		guy.forward(size)
		guy.right(144)


def many_stars(move, turn, size):
	draw_star(size)
	guy.penup()
	guy.forward(move)
	guy.right(turn)
	guy.pendown()


for i in range(5):
	many_stars(350, 144, 100)


guy.showturtle()

window.mainloop()
"""
import turtle

turtle.setup(500, 500)
wn = turtle.Screen()
wn.title("Turtle Keys")
move = turtle.Turtle()

def k1():
	move.forward(45)

def k2():
	move.left(45)

def k3():
	move.right(45)

def k4():
	move.back(45)

wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")

wn.listen()
wn.exitonclick()
