import turtle



def draw_triangle(turtle, length):
    turtle.forward(length)
    turtle.left(160)
    turtle.forward(length)
    turtle.left(160)
    turtle.forward(length)
    turtle.left(160)


def draw_art():
    window = turtle.Screen()
    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.color("blue")
    turt.speed(20)

    for i in range (0,20):
        turt.left(10)
        draw_triangle(turt, 100)

    turt.setx(50)
    turt.sety(0)
    turt.left(190)
    turt.forward(200)


    window.exitonclick()


draw_art()
