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


def draw_Square(t, size):
    for c in range(4):
        t.forward(size)
        t.left(90)


draw_Square(guy, 70)

window.mainloop()  # closes the window ater it opnes
