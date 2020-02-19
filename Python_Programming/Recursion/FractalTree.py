import turtle


def tree(branch_len, my_turtle):
    if branch_len > 5:
        my_turtle.width(.1 * branch_len)
        my_turtle.forward(branch_len)
        my_turtle.right(20)
        tree(branch_len - 15, my_turtle)
        my_turtle.left(40)
        tree(branch_len - 15, my_turtle)
        my_turtle.right(20)
        my_turtle.backward(branch_len)


if __name__ == '__main__':
    my_turtle = turtle.Turtle()
    screen = turtle.Screen()
    branch_length = 75
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.back(branch_length + 25)
    my_turtle.down()
    my_turtle.color("green")
    tree(branch_length, my_turtle)
    screen.exitonclick()
