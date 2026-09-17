import turtle

screen = turtle.Screen()
screen.setup(600, 800, 0, 0)
t = turtle.Turtle()
t.speed(5)
t.pensize(3)

def draw_pedal(radius, arc_angle):
    for i in range(2):
        t.circle(radius, arc_angle)
        t.left(180 - arc_angle)
        
def draw_flower(petals, radius, arc_angle):
    turn = 360 / petals
    for i in range(petals):
        draw_pedal(radius, arc_angle)
        t.left(turn)
        t.forward(10)