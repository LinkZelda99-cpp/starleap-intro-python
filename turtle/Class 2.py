import turtle # Import the turtle graphics library

screen = turtle.Screen() # Create a screen object to display the turtle graphics
screen.setup(600, 800, 0, 0) # Setup the screen with width 600, height 800, and position at (0, 0)

t = turtle.Turtle() # Create a turtle object to draw on the screen

t.forward(100)  # Move the turtle forward by 100 units
t.right(90)  # Turn the turtle right by 90 degrees
t.backward(100)  # Move the turtle backward by 100 units
t.left(90)  # Turn the turtle left by 90 degrees
t.pendown()  # Lower the turtle's pen to start drawing
t.forward(100)  # Move the turtle forward by 100 units
t.forward(100)
t.right(45)
t.forward(20)
t.left(45)
t.forward(100) 
screen.mainloop()  # Keep the window open and process events