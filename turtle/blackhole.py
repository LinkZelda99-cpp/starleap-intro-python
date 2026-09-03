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


# import random
# import math
# import turtle

# # ============================================================
# # SCREEN
# # ============================================================

# screen = turtle.Screen()
# screen.setup(width=1.0, height=1.0)
# screen.getcanvas().winfo_toplevel().attributes("-fullscreen", True)
# screen.getcanvas().update_idletasks()
# screen.bgcolor("black")
# screen.tracer(0)

# half_width = screen.window_width() // 2
# half_height = screen.window_height() // 2


# # ============================================================
# # BACKGROUND
# # ============================================================

# background = turtle.Turtle(visible=False)
# background.speed(0)
# background.penup()

# random.seed(42)

# lensed_stars = []


# # ============================================================
# # GRAVITATIONAL LENSING
# # ============================================================

# def draw_lensed_star(x, y, size, color):
#     """
#     Draw a background star with an approximation of
#     gravitational lensing.
#     """

#     radius = math.hypot(x, y)

#     if radius < 900:
#         angle = math.atan2(y, x)

#         # Stronger bending closer to the black hole.
#         strength = 9000 / max(radius * radius, 2500)

#         # Fade the effect with distance.
#         strength *= max(
#             0.0,
#             1.0 - radius / 900
#         )

#         strength = min(strength, 1.25)

#         # Bend light tangentially around the black hole.
#         if y >= 0:
#             apparent_angle = angle + strength
#         else:
#             apparent_angle = angle - strength

#         # Stretch the apparent position outward.
#         apparent_radius = radius * (
#             1.0 + strength * 0.55
#         )

#         px = apparent_radius * math.cos(apparent_angle)
#         py = apparent_radius * math.sin(apparent_angle)

#         # Save strongly lensed stars for the animated ring.
#         if radius < 500:
#             lensed_stars.append(
#                 (
#                     radius,
#                     px,
#                     py,
#                     apparent_angle,
#                     size,
#                     color,
#                     strength
#                 )
#             )

#         x = px
#         y = py

#     background.goto(x, y)
#     background.dot(size, color)


# # ============================================================
# # NEBULA
# # ============================================================

# for _ in range(650):

#     background.goto(
#         random.randint(-half_width, half_width),
#         random.randint(-half_height, half_height)
#     )

#     background.dot(
#         random.randint(6, 42),
#         random.choice(
#             (
#                 "#080b24",
#                 "#0b1030",
#                 "#101044",
#                 "#151044",
#                 "#0b2445",
#                 "#102b4d",
#                 "#160d38"
#             )
#         )
#     )

# screen.update()


# # ============================================================
# # STAR FIELD
# # ============================================================

# for _ in range(2400):

#     draw_lensed_star(
#         random.randint(-half_width, half_width),
#         random.randint(-half_height, half_height),
#         random.choice(
#             (1, 1, 1, 1, 2, 2, 3)
#         ),
#         random.choice(
#             (
#                 "#ffffff",
#                 "#dbeafe",
#                 "#bfdbfe",
#                 "#fef3c7"
#             )
#         )
#     )

# screen.update()


# # ============================================================
# # FOREGROUND STARS
# # ============================================================

# for _ in range(180):

#     background.goto(
#         random.randint(-half_width, half_width),
#         random.randint(-half_height, half_height)
#     )

#     background.dot(
#         random.randint(4, 7),
#         random.choice(
#             (
#                 "#ffffff",
#                 "#93c5fd",
#                 "#c4b5fd",
#                 "#fde68a",
#                 "#f9a8d4"
#             )
#         )
#     )

# screen.update()


# # ============================================================
# # ANIMATION TURTLES
# # ============================================================

# lensed_light = turtle.Turtle(visible=False)
# lensed_light.speed(0)
# lensed_light.penup()

# t = turtle.Turtle(visible=False)
# t.speed(0)
# t.penup()

# animation_delay = round(1000 / 30)


# # ============================================================
# # LENSED BACKGROUND LIGHT
# # ============================================================

# def draw_nearby_lensed_light(ring_radius):
#     """
#     Draw background light that has been strongly bent around
#     the black hole.
#     """

#     lensed_light.clear()

#     for (
#         star_radius,
#         px,
#         py,
#         apparent,
#         size,
#         color,
#         strength
#     ) in lensed_stars:

#         if abs(star_radius - ring_radius) <= 35:

#             # Stronger lensing = longer apparent arc.
#             arc = min(
#                 55,
#                 max(
#                     3,
#                     int(8 + strength * 30)
#                 )
#             )

#             bent_radius = math.hypot(px, py)

#             lensed_light.goto(px, py)

#             # Light travels tangentially.
#             lensed_light.setheading(
#                 math.degrees(apparent) + 90
#             )

#             lensed_light.pencolor(color)
#             lensed_light.pensize(
#                 max(1, size)
#             )

#             lensed_light.pendown()

#             lensed_light.circle(
#                 max(10, bent_radius),
#                 arc
#             )

#             lensed_light.penup()


# # ============================================================
# # LARGE EINSTEIN RING
# # ============================================================

# def light_ring(radius, width):
#     """
#     Draw the large gravitationally lensed Einstein ring.

#     This is intentionally far larger than the photon ring.
#     """

#     random.seed(int(radius * 10))

#     # --------------------------------------------------------
#     # BROAD OUTER GLOW
#     # --------------------------------------------------------

#     glow_layers = (
#         ("#16263a", width * 2.8),
#         ("#253d50", width * 2.1),
#         ("#66503b", width * 1.5),
#         ("#b87345", width * 1.1),
#     )

#     for color, thickness in glow_layers:

#         t.pencolor(color)
#         t.pensize(
#             max(1, int(thickness))
#         )

#         t.goto(radius, 0)
#         t.setheading(90)

#         t.pendown()
#         t.circle(radius, 360)
#         t.penup()

#     # --------------------------------------------------------
#     # BRIGHT BROKEN LIGHT
#     # --------------------------------------------------------

#     hot_colors = (
#         "#dbeafe",
#         "#e0f2fe",
#         "#fff7ed",
#         "#fed7aa",
#         "#fef3c7",
#         "#ffffff",
#     )

#     for _ in range(
#         max(100, int(radius * 0.7))
#     ):

#         ring_radius = radius + random.uniform(
#             -width * 0.45,
#             width * 0.45
#         )

#         start = random.randrange(360)
#         extent = random.randint(2, 12)

#         t.pencolor(
#             random.choice(hot_colors)
#         )

#         t.pensize(
#             random.choice(
#                 (
#                     1,
#                     1,
#                     1,
#                     2,
#                     max(1, int(width * 0.12))
#                 )
#             )
#         )

#         angle = math.radians(start)

#         t.goto(
#             ring_radius * math.cos(angle),
#             ring_radius * math.sin(angle)
#         )

#         t.setheading(start + 90)

#         t.pendown()
#         t.circle(
#             ring_radius,
#             extent
#         )
#         t.penup()

#     # --------------------------------------------------------
#     # BRIGHT HOT SPOTS
#     # --------------------------------------------------------

#     for _ in range(
#         max(25, int(radius * 0.15))
#     ):

#         angle = math.radians(
#             random.randrange(360)
#         )

#         spot_radius = radius + random.uniform(
#             -width * 0.25,
#             width * 0.25
#         )

#         t.goto(
#             spot_radius * math.cos(angle),
#             spot_radius * math.sin(angle)
#         )

#         t.dot(
#             random.randint(
#                 1,
#                 max(2, int(width * 0.35))
#             ),
#             random.choice(hot_colors)
#         )


# # ============================================================
# # PHOTON RING
# # ============================================================

# def photon_ring(size):
#     """
#     Draw the small, extremely bright photon ring immediately
#     outside the black-hole shadow.
#     """

#     radius = size * 1.55

#     # --------------------------------------------------------
#     # SOFT PHOTON-RING GLOW
#     # --------------------------------------------------------

#     glow_layers = (
#         ("#101c28", 5.0),
#         ("#243b4a", 3.5),
#         ("#526b75", 2.2),
#         ("#b9d5dc", 1.4),
#     )

#     for color, multiplier in glow_layers:

#         t.pencolor(color)

#         t.pensize(
#             max(
#                 1,
#                 int(size * multiplier * 0.08)
#             )
#         )

#         t.goto(radius, 0)
#         t.setheading(90)

#         t.pendown()
#         t.circle(radius, 360)
#         t.penup()

#     # --------------------------------------------------------
#     # IRREGULAR HOT LIGHT
#     # --------------------------------------------------------

#     hot_colors = (
#         "#ffffff",
#         "#fefce8",
#         "#e0f2fe",
#         "#fef3c7",
#         "#dbeafe",
#     )

#     random.seed(int(size * 37))

#     for _ in range(
#         max(30, int(size * 1.8))
#     ):

#         r = radius + random.uniform(
#             -size * 0.12,
#             size * 0.12
#         )

#         start = random.uniform(
#             0,
#             360
#         )

#         extent = random.uniform(
#             1,
#             8
#         )

#         t.goto(
#             r * math.cos(
#                 math.radians(start)
#             ),
#             r * math.sin(
#                 math.radians(start)
#             )
#         )

#         t.setheading(
#             start + 90
#         )

#         t.pencolor(
#             random.choice(hot_colors)
#         )

#         t.pensize(
#             random.choice(
#                 (1, 1, 1, 2)
#             )
#         )

#         t.pendown()
#         t.circle(r, extent)
#         t.penup()


# # ============================================================
# # BLACK HOLE
# # ============================================================

# def black_hole(size: float = 2):
#     """
#     Animate the black hole growing.

#     size = radius of the black-hole shadow.
#     """

#     if size > 35:
#         return

#     t.clear()

#     # ========================================================
#     # LARGE EINSTEIN RING
#     # ========================================================

#     outer_ring_radius = size * 8.5

#     max_ring = min(
#         half_width,
#         half_height
#     ) * 0.72

#     outer_ring_radius = min(
#         outer_ring_radius,
#         max_ring
#     )

#     outer_ring_width = max(
#         2,
#         outer_ring_radius * 0.035
#     )

#     draw_nearby_lensed_light(
#         outer_ring_radius
#     )

#     light_ring(
#         outer_ring_radius,
#         outer_ring_width
#     )

#     # ========================================================
#     # PHOTON RING
#     # ========================================================

#     photon_ring(size)

#     # ========================================================
#     # BLACK-HOLE SHADOW
#     # ========================================================

#     # Outer dark halo.
#     t.goto(0, 0)

#     t.dot(
#         int(size * 2.5),
#         "#030303"
#     )

#     # Actual black shadow.
#     t.dot(
#         int(size * 2.0),
#         "black"
#     )

#     screen.update()

#     # Continue growing.
#     screen.ontimer(
#         lambda: black_hole(
#             size + 2 / 3
#         ),
#         animation_delay
#     )


# # ============================================================
# # START
# # ============================================================

# black_hole()

# screen.mainloop()