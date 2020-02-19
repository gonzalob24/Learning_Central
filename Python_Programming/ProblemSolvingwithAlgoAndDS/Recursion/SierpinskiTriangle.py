import turtle


def draw_triangle(points, color,  my_turle):
    my_turtle.fillcolor(color)
    my_turtle.penup()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def mid_point(point1, point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2


def sierpinski_triangle(points, degree, my_turtle):
    color_map = ['blue', 'red', 'green', 'orange', 'yellow', 'violet', 'white']

    draw_triangle(points, color_map[degree], my_turtle)
    if degree > 0:
        sierpinski_triangle([points[0],
                            mid_point(points[0], points[1]),
                            mid_point(points[0], points[2])],
                            degree - 1, my_turtle)
        sierpinski_triangle([points[1],
                            mid_point(points[0], points[1]),
                            mid_point(points[1], points[2])],
                            degree - 1, my_turtle)
        sierpinski_triangle([points[2],
                            mid_point(points[2], points[1]),
                            mid_point(points[0], points[2])],
                            degree - 1, my_turtle)


if __name__ == '__main__':
    my_turtle = turtle.Turtle()
    wn = turtle.Screen()
    my_turtle.speed("slowest")
    myPoints = [[-100, -50], [0, 100], [100, -50]]
    sierpinski_triangle(myPoints, 3, my_turtle)
    wn.exitonclick()
