#Making decision structure for shape and other
import turtle 
shape = input('Shape: ')
if shape == 'Circle':
    pen_color = input('Enter the pen color you like:  ')
    if pen_color == 'Red':
            turtle.pencolor(pen_color)
            turtle.Begin_filling()
            turtle.fillcolor('pink')
            turtle.circle(50)
        
    elif pen_color == 'Blue':
        turtle.pencolor(pen_color)
        turtle.fillcolor('green')
        turtle.circle(50)
    else:
        turtle.pencolor(pen_color)
        turtle.fillcolor('orange')
        turtle.circle(50)
else:
    fill_color = input('Enter the fill color for the square:  ')
    if fill_color == 'Red':
        turtle.pencolor('pink')
    elif fill_color == 'Blue':
        turtle.pencolor('green')
    else:
        turtle.pencolor('orange')

        
            
        