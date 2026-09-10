import math
import random
import turtle

def random_rgb():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


def create_turtle():
    t = turtle.Turtle()
    t.speed(random.randint(1, 10))
    t.penup()
    t.color(random_rgb())
    t.pensize(random.randint(5, 20))
    t.pendown()
    return t


def super_random_turtle():
    turtle.colormode(255)

    screen = turtle.Screen()
    width = screen.window_width() // 2
    height = screen.window_height() // 2
    screen.tracer(0)
    # Create a random number of turtles
    turtle_count = random.randint(5, 50)

    turtles = []

    for _ in range(turtle_count):
        turtles.append(create_turtle())

    # Control all turtles
    num = 99_999_999

    while num > 0:
        for t in turtles:
            t.begin_fill()
            t.color(random_rgb())
            # screen.bgcolor(random_rgb())
            distance = random.randint(10, 100)
            angle = random.randint(0, 360)

            # Calculate the next position
            x, y = t.position()
            heading = t.heading()

            rad = math.radians(heading)

            new_x = x + math.cos(rad) * distance
            new_y = y + math.sin(rad) * distance

            # Check if the next position is inside the screen
            if -width < new_x < width and -height < new_y < height:
                t.forward(distance)
            else:
                # Turn if the turtle would leave the screen
                t.right(random.randint(0, 360))

            t.right(angle)
            t.end_fill()
        num -= 1
        screen.update()
        
super_random_turtle()
turtle.done()