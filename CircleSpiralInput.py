# CircleSpiralInput.py
# Billy Ridgeway
# Draws a colorful circle spiral with the number of sides input by the user.

import turtle               # Imports turtle graphics.
t = turtle.Pen()            # Creates a new turtle called t.
t.speed(0)                  # Sets the pen's speed to fast.
turtle.bgcolor("black")     # Sets the background color to black.

# Set up a list of any 8 valid Python color names.
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white"]

# Ask the user for the number of sides between 1 and 8 with a default of 4.
sides = int(turtle.numinput("Number of sides", "How many sides do you want (1-8)?", 4, 1, 8))

# Draw a colorful spiral with the user specified number of circles.
for x in range(90):
    t.pencolor( colors[x % sides] )     # Only use the correct number of colors.
    t.circle(x)                         # Draws 90 circles.
    t.left(360/sides + 1)               # Turn 360 degrees divided by the number of sides plus 1.
    t.width( x * sides / 200)           # Make the pen larger as it travels out from the center of the spiral.
   
