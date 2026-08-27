import turtle

screen = turtle.Screen()
screen.setup(600, 800, 0, 0)
screen.bgcolor("black")

size = 100

t = turtle.Turtle()
t.speed(-1)
t.pendown()
t.color("yellow")
t.fillcolor("yellow")

# Draw the first filled triangle

t.begin_fill()
t.left(90)
t.left(90)
t.forward(size)
t.right(120)
t.forward(size)
t.right(120)
t.forward(size)
t.right(120)
t.forward(size)
t.left(60)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.end_fill()

# Move into position for the second filled triangle
t.right(180)
t.forward(size)

# Draw the second filled triangle
t.begin_fill()
t.left(120)
t.forward(size)
t.right(120)
t.forward(size)
t.right(120)
t.forward(size)
t.end_fill()

# Hide the turtle and display the window
t.hideturtle()
screen.mainloop()