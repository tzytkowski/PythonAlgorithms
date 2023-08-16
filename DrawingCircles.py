import turtle
'''
#variables
radius = int()
pen_size = int()
horizontal = int()
colors = ["red", "blue", "yellow", "green"]

radius = 25
pen_size = 2
horizontal = -200

# Loop to draw circles
for count in range(0, 4):
    # Set the turtles pen size and fill color
    turtle.pensize(pen_size)
    turtle.fillcolor(colors[count])

    # Move turtle
    turtle.penup()
    turtle.goto(horizontal, 0)
    turtle.pendown()

    # Draw the circle
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    # Reset the turtles radius and pen size
    radius = radius + 20
    pen_size = pen_size + 2

    # Move the turtles starting point
    horizontal = horizontal + 75
    turtle.penup()
    turtle.goto(horizontal, 0)
    turtle.pendown()
'''

import turtle
import time
import random
turtle.setup(600, 600)
turtle.reset()
time.sleep(1)

colors = ['red', 'green', 'blue', 'yellow']
turtle.write("Ready for more circles?", align='center', font=("Arial", 16, "bold"))
for count in range(20):
    radius = random.randint(25, 125)
    pen_size = random.randint(1, 10)
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    # Pen size
    turtle.pensize(pen_size)

    # Color
    turtle.fillcolor(colors[random.randint(0, 3)])

    # Moving the pen
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Drawing circle
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
# End loop


turtle.exitonclick()
