import turtle
import random
import time 

def Climbing(color, depth):
    turtle.shape('turtle')
    depth = turtle.pensize(depth)
    color = turtle.pencolor(color)
    for x in range(4):
        turtle.forward(50)
        turtle.lt(90)
        turtle.forward(50)
        turtle.rt(90)
    turtle.forward(50)
    turtle.write('Hurray! Made it to the top', align='center', font=("Arial", 16, "bold"))

def Swimming(color, thickness):
    # Asking user for input
    color = input('Pick a color: ')
    thickness = int(input('Pick a thickness: '))
    turtle.pencolor(color)
    turtle.pensize(thickness)
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(80)
    turtle.end_fill()
    turtle.rt(90)
    turtle.forward(10)
    turtle.lt(90)
    turtle.pencolor('yellow')
    turtle.circle(100)
    turtle.write("Yeah! I'm swimming", align='center', font=("Arial", 16, "bold"))
    turtle.pencolor('black')
    turtle.color('green')
    turtle.shape('turtle')

def Eating():
    import random
    # Declare variables
    colors = ["red", "green", "red", "yellow"]
    x = -150
    y = -150
    u = -150
    v = -150

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for i in range(0, 4):
        turtle.fillcolor(colors[i])
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x + 10, y + 10)
        turtle.pendown()
        x = x + 10
        y = y + 10

# Back to starting point
    turtle.penup()
    turtle.goto(u, v)
    turtle.pendown()
    turtle.shape("turtle")
    turtle.color("green")
    
    # White circles "eating" colored circles
    for j in range(0, 4):
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(u + 10, v + 10)
        turtle.pendown()
        turtle.color("green")
        u = u + 10
        v = v + 10
    turtle.color("black")
    turtle.write("Wow! What a great meal!", align='center', font=("Arial", 14, "bold"))
    


def Sleeping():
    # Outer Circle
    turtle.fillcolor('brown')
    turtle.penup()
    turtle.goto(150, -150)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(120)
        turtle.lt(90)
    turtle.end_fill()
    # Inner circle
    turtle.shape('turtle')
    turtle.color('green')
    turtle.fillcolor('white')
    turtle.penup()
    turtle.goto(195, -90)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(30)
        turtle.lt(90)
    turtle.end_fill()
    turtle.color('black')
    turtle.write("Good Night!", align='center', font=("Arial", 14, "bold"))




def main():
    Climbing('red', 4)
    time.sleep(3)
    turtle.reset()
    Swimming('blue', 2)
    time.sleep(3)
    turtle.reset()
    Eating()
    time.sleep(3)
    turtle.reset()
    Sleeping()
    time.sleep(3)


main()