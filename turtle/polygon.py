import turtle
screen = turtle.Screen()
screen.setup(600, 800, 0, 0)
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(-1)
t.penup()
t.goto(0, 400)
t.pendown()
def draw_polygon(sides, length):
    for i in range(sides):
        t.forward(length)
        t.right(360 / sides)
draw_polygon(2500, 1)
t.hideturtle()
screen.mainloop()