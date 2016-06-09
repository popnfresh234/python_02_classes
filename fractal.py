import turtle

def draw_triangle(turtle, length):
    for i in range (0,3):
        turtle.forward(length)
        turtle.left(120)

def draw_fractal():
    window = turtle.Screen()
    length = 200
    fractal_turtle = turtle.Turtle()
    fractal_turtle.color("blue")
    fractal_turtle.shape("turtle")
    fractal_turtle.speed(2)
    for i in range (0,10):
        draw_triangle(fractal_turtle, length)
        length = length/2
    window.exitonclick()

draw_fractal()
