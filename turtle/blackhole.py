import random
import math
import turtle

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)
screen.getcanvas().update_idletasks()
screen.bgcolor("black")
screen.tracer(0)

half_width = screen.window_width() // 2
half_height = screen.window_height() // 2

background = turtle.Turtle(visible=False)
background.speed(0)
background.penup()
random.seed(42)
lensed_stars = []

def draw_lensed_star(x, y, size, color):
    """Draw a star as seen through the black hole's gravitational lens.

    This is a visual approximation of gravitational lensing: light passing
    close to the event horizon is deflected, so stars behind the hole appear
    stretched into tangential arcs around it.
    """
    radius = math.hypot(x, y)
    if radius < 700:
        strength = max(0.0, 1.0 - radius / 700) ** 2
        bend = 0.75 * strength / max(radius / 120, 0.45)
        angle = math.atan2(y, x)
        apparent = angle + bend * (1 if y >= 0 else -1)
        apparent_radius = radius + 22 * strength
        px = apparent_radius * math.cos(apparent)
        py = apparent_radius * math.sin(apparent)

        if radius < 430:
            lensed_stars.append((radius, px, py, apparent, size, color, strength))
            return
        x, y = px, py

    background.goto(x, y)
    background.dot(size, color)

for _ in range(650):
    background.goto(random.randint(-half_width, half_width),
                   random.randint(-half_height, half_height))
    background.dot(random.randint(6, 42), random.choice(
        ("#080b24", "#0b1030", "#101044", "#151044", "#0b2445",
         "#102b4d", "#160d38")))
screen.update()

for _ in range(2400):
    draw_lensed_star(random.randint(-half_width, half_width),
                     random.randint(-half_height, half_height),
                     random.choice((1, 1, 1, 1, 2, 2, 3)), random.choice(
                         ("#ffffff", "#dbeafe", "#bfdbfe", "#fef3c7")))
screen.update()

for _ in range(180):
    background.goto(random.randint(-half_width, half_width),
                   random.randint(-half_height, half_height))
    background.dot(random.randint(4, 7), random.choice(
        ("#ffffff", "#93c5fd", "#c4b5fd", "#fde68a", "#f9a8d4")))

screen.update()
lensed_light = turtle.Turtle(visible=False)
lensed_light.speed(0)
lensed_light.penup()
t = turtle.Turtle(visible=False)
t.speed(100)
t.penup()
animation_delay = round(1000 / 30)

def draw_nearby_lensed_light(ring_radius):
    """Reveal bent light only as the accretion ring approaches it."""
    lensed_light.clear()
    for star_radius, px, py, apparent, size, color, strength in lensed_stars:
        if abs(star_radius - ring_radius) <= 28:
            lensed_light.goto(px, py)
            lensed_light.setheading(math.degrees(apparent) + 90)
            lensed_light.pencolor(color)
            lensed_light.pensize(max(1, size))
            lensed_light.pendown()
            lensed_light.circle(max(8, star_radius + 22 * strength),
                                4 + int(12 * strength))
            lensed_light.penup()

def light_ring(radius, width):
    """Draw a bright, layered accretion ring with broken, glowing arcs."""
    random.seed(int(radius * 10))
    glow = ("#351016", "#6b1d1b", "#a8320e", "#e85d12")
    fire = ("#ea580c", "#fb923c", "#fbbf24", "#fff7ad")

    for layer, color in enumerate(glow, 1):
        t.pencolor(color)
        t.pensize(max(1, int(width * (len(glow) - layer + 1) / 2.8)))
        t.goto(radius, 0)
        t.setheading(90)
        t.pendown()
        t.circle(radius, 360)
        t.penup()

    for _ in range(max(24, int(radius * 0.28))):
        ring_radius = radius + random.uniform(-width * 0.38, width * 0.38)
        start = random.randrange(360)
        extent = random.randint(8, 24)
        t.pencolor(random.choice(fire))
        t.pensize(random.randint(1, max(1, int(width * 0.16))))
        angle = math.radians(start)
        t.goto(ring_radius * math.cos(angle), ring_radius * math.sin(angle))
        t.setheading(start + 90)
        t.pendown()
        t.circle(ring_radius, extent)
        t.penup()

    for _ in range(max(6, int(radius * 0.06))):
        angle = math.radians(random.randrange(360))
        spot_radius = radius + random.uniform(-width * 0.25, width * 0.25)
        t.goto(spot_radius * math.cos(angle), spot_radius * math.sin(angle))
        t.dot(random.randint(2, max(2, int(width * 0.45))), random.choice(fire))

def black_hole(size: float = 2):
    """Animate a black hole growing from the center."""
    if size > 520:
        return

    t.clear()
    t.goto(0, 0)
    t.dot(int(size), "black")
    ring_radius = size * 0.52 + max(1, size // 40)
    draw_nearby_lensed_light(ring_radius)
    light_ring(ring_radius, max(2, size // 25))
    screen.update()
    screen.ontimer(lambda: black_hole(size + 2 / 3), animation_delay)
black_hole()
screen.mainloop()
