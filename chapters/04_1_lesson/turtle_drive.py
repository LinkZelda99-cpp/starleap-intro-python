import turtle
import time
import random

X_BOUND = 300
Y_BOUND = 300

STEP_SIZE = 5
TURN_SIZE = 5

screen = turtle.Screen()
turtle.tracer(False)
turtle.screensize(2 * X_BOUND + 10, 2 * Y_BOUND + 10)
screen.listen()

turtles: list[turtle.Turtle] = []

def add_turtle():
    global turtles
    t = turtle.Turtle()
    turtle.colormode(255)
    t.color((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    t.penup()
    x = random.randint(-X_BOUND, X_BOUND)
    y = random.randint(-Y_BOUND, Y_BOUND)
    t.goto(x, y)
    t.pendown()
    turtles.append(t)
    t.position()
screen.onkeypress(add_turtle, "t")

def fwd():
    for t in turtles:
        t.fd(STEP_SIZE)
screen.onkeypress(fwd, "Up")

def lt():
    for t in turtles:
        t.lt(TURN_SIZE)
screen.onkeypress(lt, "Left")

def rt():
    for t in turtles:
        t.rt(TURN_SIZE)
screen.onkeypress(rt, "Right")

def remove_turtle():
    if len(turtles) == 0:
        return
    t = turtles.pop(0)
    t.clear()
    t.hideturtle()
screen.onkeypress(remove_turtle, "-")


while True:
    time.sleep(0.05)
    screen.update()

turtle.mainloop()