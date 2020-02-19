# program that will draw a five point star

import turtle

window = turtle.Screen()

guy = turtle.Turtle()
guy.shape("turtle")
guy.pensize(5)
guy.hideturtle()
guy.color("blue", "red")
guy.speed(10)

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


# guy.showturtle()

window.mainloop()
