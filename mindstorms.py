import turtle

def draw_square(turtle):
    for i in range (0,4):
        turtle.forward(100)
        turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)
    for i in range (0,36):
        draw_square(brad)
        brad.right(10)

    #angie = turtle.Turtle()
    #angie.shape("turtle")
    #angie.color("blue")
    #angie.circle(100)

    window.exitonclick()

draw_art()
