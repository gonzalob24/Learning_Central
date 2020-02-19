import turtle

window = turtle.Screen()

window.bgcolor("lightpink")

pointer = turtle.Turtle()
pointer.shape("turtle")
pointer.pensize(3)

pointer.color("blue")

pointer.hideturtle()
pointer.speed(5)
pointer.stamp()

for i in range(12):
	pointer.penup()
	pointer.right(30 * i)
	pointer.forward(140)
	pointer.pendown()
	pointer.forward(15)
	pointer.penup()
	pointer.forward(15)
	pointer.stamp()
	pointer.home()
	

window.mainloop()


