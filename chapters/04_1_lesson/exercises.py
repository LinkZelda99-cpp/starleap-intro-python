import turtle
turtle.bgcolor("black")
a = turtle.Turtle()
a.color("red")
a.speed(0)
# b = turtle.Turtle()
# c = turtle.Turtle()
# d = turtle.Turtle()
# a.forward(100)
# b.left(90)
# b.forward(100)
# c.right(90)
# c.forward(100)
# d.left(180)
# d.forward(100)
def draw_squares():
    n = 100
    for i in range(4):
        while i > 0:
            a.fd(n)
            a.lt(90)
            n -= 10
    turtle.done()
#draw_squares()
def square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)
    turtle.done()
#square(a, 200)

def polygon(t, length, n):
    for i in range(n):
        t.forward(length)
        t.left(360 / n)
    turtle.done()
#polygon(a, 100, 4)

def circle(t, radius):
    circumference = 2 * 3.14159 * radius
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, length, n)
    
def arc(t, radius, angle):
    circumference = 2 * 3.14159 * radius
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, length, n)
arc(a, 100, 90)
# # ...existing code...
# import os
# import sys
# import urllib.request
# import tkinter as tk

# try:
#     from PIL import Image, ImageTk
# except Exception:
#     print("Pillow is required. Install with: pip install pillow")
#     sys.exit(1)

# MONA_URL = "https://upload.wikimedia.org/wikipedia/commons/6/6a/Mona_Lisa.jpg"
# LOCAL_NAME = "mona_lisa.jpg"

# def ensure_image(path=LOCAL_NAME):
#     if not os.path.exists(path):
#         print("Downloading Mona Lisa (public domain)...")
#         data = urllib.request.urlopen(MONA_URL).read()
#         with open(path, "wb") as f:
#             f.write(data)
#     return path

# def pixelate(img: Image.Image, pixel_size: int) -> Image.Image:
#     w, h = img.size
#     small = img.resize((max(1, w // pixel_size), max(1, h // pixel_size)), Image.NEAREST)
#     return small.resize((w, h), Image.NEAREST)

# class MonaApp(tk.Tk):
#     def __init__(self, image_path):
#         super().__init__()
#         self.title("Mona Lisa — tkinter + Pillow")
#         self.img_orig = Image.open(image_path).convert("RGB")
#         self.canvas = tk.Canvas(self, width=self.img_orig.width, height=self.img_orig.height)
#         self.canvas.pack()
#         ctrl = tk.Frame(self)
#         ctrl.pack(fill="x", pady=4)
#         tk.Button(ctrl, text="Full detail", command=self.show_full).pack(side="left", padx=4)
#         tk.Button(ctrl, text="Pixelate 4", command=lambda: self.show_pixelated(4)).pack(side="left")
#         tk.Button(ctrl, text="Pixelate 8", command=lambda: self.show_pixelated(8)).pack(side="left")
#         tk.Button(ctrl, text="Pixelate 16", command=lambda: self.show_pixelated(16)).pack(side="left")
#         tk.Button(ctrl, text="Quit", command=self.destroy).pack(side="right", padx=4)
#         self._photo = None
#         self.show_full()

#     def show_full(self):
#         self._display(self.img_orig)

#     def show_pixelated(self, size):
#         img = pixelate(self.img_orig, size)
#         self._display(img)

#     def _display(self, img: Image.Image):
#         self.canvas.config(width=img.width, height=img.height)
#         self._photo = ImageTk.PhotoImage(img)
#         self.canvas.create_image(0, 0, anchor="nw", image=self._photo)

# if __name__ == "__main__":
#     path = ensure_image()
#     app = MonaApp(path)
#     app.mainloop()
# # ...existing code...