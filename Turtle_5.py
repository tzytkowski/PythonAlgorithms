import turtle
import time
import random


#Justin Johnson Code
def drawboard():
    turtle.reset()
    turtle.setup(600, 600)
    turtle.shape("classic")
    turtle.speed(10)
    for i in range(2):
        for u in range(2):
            turtle.penup()
            turtle.goto(-300, 100 - 200 * u)
            turtle.pendown()
            turtle.forward(600)
        turtle.penup()
        turtle.goto(-100 + 200 * i, 300)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(600)
        turtle.left(90)


#Heather Casto-Thatcher Code below here****
#write the numbers on the board 1 - 9
def numbers():
  #define variable
  number = int()
  number = 1

  def write(message):
    turtle.pencolor("black")
    turtle.write(message, align = ("center"), font = ("Arial",60,"bold"))
    
  for r in range(3):
    for c in range(3):
        turtle.penup()
        turtle.goto(-200 + 200 * c, 150 - 200 * r)
        turtle.pendown()
        write(number)
        number = number + 1


#Tyler Zytkowski code below here ************************************************
def UpdateBoard(intGuess, rightOrWrong):
    #int_guess = int()
    #int_number = int()
    coordinates = [[-100, 100],
                   [100, 100],
                   [300, 100],
                   [-100, -100],
                   [100, -100],
                   [300, -100],
                   [-100, -300],
                   [100, -300],
                   [300, -300]]
    winningposition = [[-200, 200],
                        [0, 200],
                        [200, 200],
                        [0, -200],
                        [0, 0],
                        [0, 200],
                        [-200, -200],
                        [0, -200],
                        [200, -200]]


    if rightOrWrong == 0:
        turtle.penup()
        turtle.goto(coordinates[intGuess - 1][0], coordinates[intGuess - 1][1])
        turtle.setheading(90)
        turtle.pendown()
        turtle.fillcolor("red")
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(200)
            turtle.lt(90)
        turtle.end_fill()
    else:
        turtle.penup()
        turtle.fillcolor("white")
        turtle.goto(coordinates[intGuess - 1][0],coordinates[intGuess - 1][1])
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(200)
            turtle.lt(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(winningposition[intGuess - 1])
        turtle.shape("turtle")
        turtle.shapesize(5, 5, 1)
        turtle.color("green")
        turtle.showturtle()
#Kelley VanBuskirk code  below here *********************************************



def sprgRunGame():
    #inputs
    intGuess = int(0)

    #internals
    intGuessNumber = int()
    intTurtlePosition = int()
    intWinner = int()
    lsAllGuesses = []
   
    
    #Justin's Function call Here
    drawboard()

    #Insert Heather's Function call Here
    numbers()

    #hide the turtle
    intTurtlePosition = random.randint(1,9)
    print("Debug - turtle at: ",intTurtlePosition)

    print("The turtle is hiding! ")
    
    while intGuessNumber < 4:
        
        intGuess = int(input("Where is the turtle?\nGuess a number between 1 and 9:  "))
        if intGuess == intTurtlePosition:
            intWinner=1
        UpdateBoard(intGuess,intWinner)
        if intWinner == 1:
            print("Congratulations, you found the turtle!")
            break
        lsAllGuesses.append(intGuess)
        lsAllGuesses.sort()
        intGuessNumber = intGuessNumber + 1
        print("You have already guessed: ",end="")
        for i in range(len(lsAllGuesses)):
            print(lsAllGuesses[i],"",end="")
        print()
    if intGuessNumber == 4:
        print("Game Over!\n The turtle was behind number "+str(intTurtlePosition)+".")
        UpdateBoard(intTurtlePosition,1)
        print()
    
    time.sleep(5)
  
  
        



def main():
    '''***************************************************************************
    *Description: 
    ******************************************************************************
    *Decomposition:
    *******************************************************************************
    *Parameters: 
    ******************************************************************************
    *Inputs:
    ******************************************************************************
    *Outputs: 
    *****************************************************************************
    *Author: K.VanBuskirk
    *Date: 
    *Reviser:
    *Date:
    ******************************************************************************
    *Revision Notes [Date,note]:
    *
    ***************************************************************************'''
    strRun = str()

    while True:
        while True:
            print("Do you want to play Hide and Seek")
            strRun = input("Enter Y for Yes or N for No:  ")
            strRun = strRun.upper()
            if strRun=="Y" or strRun=="N":
                break
            else:
                print()
                print("You did not enter a correct choice.")
                print()
        if strRun == "N":
            break
        sprgRunGame()


#**************************No edits below hear **************************************
main()
