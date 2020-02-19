# Modify the turtle bar chart program from the previous chapter so that the bar for any value of 200
# or more is filled with red, values between [100 and 200) are filled yellow, and bars representing
# values less than 100 are filled green.


import turtle


def draw_bar(t, height):
	tess_color(height)
	t.left(90)
	t.begin_fill()
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


def tess_color(height):
	if height >= 200:
		tess.color("blue", "red")
	elif height >= 100 and height < 200:
		tess.color("blue", "yellow")
	else:
		tess.color("blue", "green")


window = turtle.Screen()		#sets up the window
window.bgcolor("lightblue")	#changes the color of the window

tess = turtle.Turtle()   	   #creates the turtle

tess.pensize(3)

xs = [48, 117, 200, 240, 160, 260, -220]

for number in xs:
	draw_bar(tess, number)

window.mainloop()
