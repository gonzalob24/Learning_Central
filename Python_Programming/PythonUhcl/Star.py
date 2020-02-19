# program that will draw a five point star

import turtle

window = turtle.Screen()

guy = turtle.Turtle()
guy.shape("turtle")
guy.pensize(5)
guy.hideturtle()
guy.color("blue", "red")

guy.right(36)
guy.forward(200)
guy.right(36)
guy.forward(-200)
guy.right(36)
guy.forward(200)
guy.right(36)
guy.forward(-200)
guy.right(36)
guy.forward(200)

guy.showturtle()

window.mainloop()
