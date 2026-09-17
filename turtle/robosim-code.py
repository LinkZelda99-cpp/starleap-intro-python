from getpass import getpass
import math
from robosim import Turtle

t = Turtle(
    username="LinkZelda99",
    password="LinkZelda0518!", # getpass("Password: "),
    url="wss://robosim.judymud.com/ws",
    room="main",
    robot=34,
)
t.speed(1)
# t.penup()
# t.goto(0, 400)
t.pendown()
# screen.tracer(0)
def draw_polygon(sides, length):
    for _ in range(sides):
        t.forward(length)
        t.right(360 / sides)
def draw_circle(radius):
    draw_polygon(360, radius * 2 * math.pi / 360)
def black_hole():
    for i in range(100):
        t.pensize(i)
        t.circle(100 - i)
black_hole()