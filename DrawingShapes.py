import turtle
import sys

# Part 1
# Variables
pen_size = int()
pen_color = str()
fill_color = str()

# Moving the pen
turtle.penup()
turtle.goto(0, 150)
turtle.pendown()

# Pick pen color for circle
pen_size = int(input('Pick a pen size between 1 - 10: '))
if pen_size < 1 or pen_size > 10:
    sys.exit('You did not pick a valid number.')
pen_color = input('What would you like the pen color to be? ')
if pen_color == 'red':
    fill_color = 'yellow'
elif pen_color == 'blue':
    fill_color = 'red'
elif pen_color == 'yellow':
    fill_color = 'green'
else:
    sys.exit('Invalid color. Program terminated.')

pen_size = pen_size
turtle.pensize(pen_size)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)

# Drawing circle
turtle.begin_fill()
# Draw circle
turtle.circle(50)
# Stopping the fill
turtle.end_fill()

# Next position
turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.pendown()

# Pick pen color for square
pen_color = input('What would you like the pen color to be? ')
if pen_color == 'red':
    fill_color = 'yellow'
elif pen_color == 'blue':
    fill_color = 'red'
elif pen_color == 'yellow':
    fill_color = 'green'
else:
    sys.exit('Invalid color. Program terminated') 

pen_size = pen_size
turtle.pensize(pen_size)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)


# Drawing square
turtle.begin_fill()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.end_fill()

# Moving location 
turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.pendown()

# Drawing triangle
# Pick pen color for triangle
pen_color = input('What would you like the pen color to be? ')
if pen_color == 'red':
    fill_color = 'yellow'
elif pen_color == 'blue':
    fill_color = 'red'
elif pen_color == 'yellow':
    fill_color = 'green'
else:
    sys.exit('Invalid color. Program terminated')

turtle.pensize(pen_size)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)


turtle.begin_fill()
turtle.right(35)
turtle.forward(125)
turtle.right(235)
turtle.forward(150)
turtle.left(127)
turtle.forward(130)
turtle.end_fill()

# Part 2
# Inputs
# 1. Ask for the shape
# 2. Ask for the location

# Output
# 1. Shapes

import turtle
import time          
time.sleep(3)
turtle.reset()
turtle.setup(600, 600) #sets up the size of the window

# Shape is either a circle or square
fill_color = str()
pen_color = str()
pen_size = int()
location = str()
user = ''

# Constants
topleft = -180, 180
topright = 180, 180
bottomleft = -180, -180
bottomright = 180, -180


# Choosing if we want a circle or square 

while user != 'Q':
    shape = input('Choose a circle or a square: ')
    if shape == 'circle':
        pen_color = input("Pick a primary color for your pen color: ")
        if pen_color == 'red':
            fill_color = 'lime green'
        elif pen_color == 'blue':
            fill_color = 'gold'
        elif pen_color == 'yellow':
            fill_color = 'magenta'
        else:
            print('You did not pick a primary color. Try again.')
            continue
    elif shape == 'square':
        fill_color = input("Pick a primary color for your fill color:  ")
        if fill_color == 'red':
            pen_color = 'spring green'
        elif fill_color == 'blue':
            pen_color = 'dark orange'
        elif fill_color == 'yellow':
            pen_color = 'blue violet'
        else:
            print('Must pick a primary color. Try again')
            continue
    elif shape != 'circle' or shape != 'square':
        print('You did not pick a circle or a square. Try again')
        continue
    location = input("Please select TL for Top Left, TR for Top Right, BL for Bottom Left or BR for Bottom Right for a location:  ")
    if location == 'TL':
        location = topleft
        pen_size = 3
    elif location == 'TR':
        location = topright
        pen_size = 5
    elif location == 'BL':
        location = bottomleft
        pen_size == 7
    elif location == 'BR':
        location = bottomright
        pen_size = 9
    else:
        print('You did not pick a valid location. Try again.')
        continue

    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.pensize(pen_size)

    # Drawing circle
    if shape == 'circle':
        turtle.penup()
        turtle.goto(location)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()

    # Drawing square
    elif shape == 'square':
        turtle.penup()
        turtle.goto(location)
        turtle.pendown()
        turtle.begin_fill()
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.end_fill()
    # Ask user if they would like to continue or not
    user = input('Would you like to continue? Enter Y to continue or Q to exit: ')



turtle.exitonclick()