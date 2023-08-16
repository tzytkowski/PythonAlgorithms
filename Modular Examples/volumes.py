#Program to calculate volumes
def main():
    #declare variables
    choice = str()

    print("This program calculates volume.")
    displayMenu()
    choice = input("Enter your choice:  ")
    while choice != "e":
        if choice == "c":
            CalculateCube()
        elif choice == "r":
            CalculateRectangle()
        else:
            CalculateSphere()
        #end if
        displayMenu()
        choice = input("Enter your choice:")
    #End while
    print("Thank you for using this program.")
def displayMenu():
    print("Enter the following letters to correspond to the shapes:")
    print("          c = cube")
    print("          r = rectangle")
    print("          s = sphere")
    print("          e = exit")
    
def CalculateCube():
    #Declare variables
    cube = float()
    side = float()
    #Ask the user for a side
    side = float(input("Enter a side:  "))
    cube = side**3
    #print cube to the user
    print("The volume is:  ", cube)

def CalculateRectangle():
    #Declare variables
    width = float()
    height = float()
    depth = float()
    rectangle = float()
    #Ask the user for the measurements
    width = float(input("Enter the width:  "))
    height = float(input("Enter the height:  "))
    depth = float(input("Enter the depth:  "))
    rectangle = width * height * depth
    #print out volume to the user
    print("The volume is:  ", rectangle)

def CalculateSphere():
    #Declare variables
    sphere = float()
    pi = 3.14159265359
    radius = float()
    #Ask user for radius
    radius = float(input("Enter the radius:  "))
    sphere = 4/3 * pi * radius**3
    print("The volume is:  ", sphere)

main()
