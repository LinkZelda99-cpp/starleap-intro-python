import turtle
import math
import random
import colorsys

# ============================================================
#                 ULTIMATE NEON TURTLE
# ============================================================

screen = turtle.Screen()
screen.setup(1100, 750)
screen.bgcolor("#05000f")
screen.title("🌈 ULTIMATE NEON TURTLE 🌈")
screen.tracer(0)

# -------------------- SETTINGS --------------------

PARTICLES = 90
RINGS = 9
SIDES = 7

# -------------------- MAIN TURTLE --------------------

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# -------------------- PARTICLES --------------------

particles = []

for _ in range(PARTICLES):
    p = turtle.Turtle()
    p.hideturtle()
    p.speed(0)
    p.penup()

    p.x = random.randint(-520, 520)
    p.y = random.randint(-350, 350)
    p.vx = random.uniform(-1.5, 1.5)
    p.vy = random.uniform(-1.5, 1.5)
    p.size = random.randint(2, 6)
    p.phase = random.random() * math.tau

    particles.append(p)

# -------------------- RAINBOW COLOR --------------------

def rainbow(offset=0):
    r, g, b = colorsys.hsv_to_rgb(
        (offset % 360) / 360,
        0.9,
        1.0
    )
    return int(r * 255), int(g * 255), int(b * 255)


def rgb_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


# -------------------- DRAW POLYGON --------------------

def polygon(turtle_obj, radius, sides, rotation, color):
    turtle_obj.color(color)
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(rotation)

    turtle_obj.forward(radius)
    turtle_obj.pendown()

    angle = 360 / sides

    for _ in range(sides):
        turtle_obj.left(angle)
        turtle_obj.forward(radius)

    turtle_obj.penup()


# -------------------- TEXT --------------------

title = turtle.Turtle()
title.hideturtle()
title.penup()

subtitle = turtle.Turtle()
subtitle.hideturtle()
subtitle.penup()

# -------------------- ANIMATION --------------------

frame = 0


def animate():
    global frame

    # Background-ish glow particles
    for i, p in enumerate(particles):

        p.x += p.vx
        p.y += p.vy

        # Wrap around screen
        if p.x > 550:
            p.x = -550
        if p.x < -550:
            p.x = 550

        if p.y > 380:
            p.y = -380
        if p.y < -380:
            p.y = 380

        pulse = (math.sin(frame * 0.04 + p.phase) + 1) / 2
        size = max(1, int(p.size * (0.6 + pulse)))

        color = rgb_hex(
            rainbow(frame * 0.8 + i * 4)
        )

        p.goto(p.x, p.y)
        p.dot(size, color)

    # Main rotating geometry
    t.clear()

    # Outer rainbow rings
    for ring in range(RINGS):
        radius = 70 + ring * 35
        rotation = frame * (1.2 + ring * 0.12)

        color = rgb_hex(
            rainbow(frame * 1.5 + ring * 35)
        )

        t.goto(0, 0)
        t.setheading(rotation)
        t.color(color)
        t.pensize(3 + (ring % 3))

        # Polygon
        t.forward(radius)
        t.pendown()

        for _ in range(SIDES):
            t.left(360 / SIDES)
            t.forward(radius)

        t.penup()

    # Inner spinning star
    t.goto(0, 0)
    t.setheading(-frame * 3)

    for i in range(18):
        color = rgb_hex(
            rainbow(frame * 2 + i * 20)
        )

        t.color(color)
        t.pensize(2 + i % 3)

        t.forward(190)
        t.backward(190)
        t.left(20)

    # Pulsating center
    pulse = 90 + math.sin(frame * 0.08) * 25

    t.goto(0, -pulse)
    t.color(
        rgb_hex(rainbow(frame * 3))
    )
    t.dot(pulse * 2)

    # Center star
    t.goto(0, 0)
    t.setheading(frame * 4)

    t.color("white")
    t.pensize(4)

    for _ in range(8):
        t.forward(75)
        t.backward(75)
        t.left(45)

    # Title
    title.clear()

    title.goto(0, 285)

    title.color(
        rgb_hex(rainbow(frame * 2))
    )

    title.write(
        "ULTIMATE NEON TURTLE",
        align="center",
        font=("Arial", 30, "bold")
    )

    # Subtitle
    subtitle.clear()
    subtitle.goto(0, -320)

    subtitle.color(
        rgb_hex(rainbow(frame * 2 + 180))
    )

    subtitle.write(
        "RAINBOW • CHAOS • TURTLE • POWER",
        align="center",
        font=("Arial", 15, "bold")
    )

    screen.update()

    frame += 1

    screen.ontimer(animate, 25)


# -------------------- START --------------------

animate()

screen.mainloop()