#This program asks the user to create and load two arrays
def main():
    #Declare variables
    NumItems = 0

    #Get the number of items for the the array
    NumItems = GetNumItems()

    #Declare your arrays now that we know how many items need to be in them
    Places = [" "] * NumItems
    Prices = [0] * NumItems

    #Fill Places and Prices
    Places, Prices = GetPlacesPrices(NumItems)

    #Print out contents of both arrays
    PrintArrays(Places, Prices, NumItems)

def GetNumItems():
    #This function validates the number of items to make sure it is a positive integer
    #This function is a value returning function
    #Declare local variables
    ValNumber = int()
    StringNumber = str()
    #Ask the user for the number
    StringNumber = input("Enter the number of items for your list:  ")
    #The best method to validate a positive integer is to use the .isdigit() method
    while not StringNumber.isdigit():
        #since the user did not give us a positive integer, we need to ask them for a new one
        StringNumber = input("You did not enter a positive integer.  Please try again:  ")

    #If we are out of the loop that means we have a good number.  Now we can return it to main
    #Convert StringNumber to an integer and assign it to ValNumber
    ValNumber = int(StringNumber)
    return ValNumber

def GetPlacesPrices(items):
    #This function is value returning and is special because it returns two value.
    #This is easy enough to do.  Make sure you return your variables in the same
    #order they were called.
    #declare local variables
    tempPlaces = [" "] * items #declares a temporary array to load items
    tempPrices = [0] * items #declares a temporary array to load items
    index = 0
    UserPlace = str()
    UserPrice = float()

    for index in range (0, items):
        #Get vacation places from the user and load in the array
        UserPlace = input("Enter a vacation spot:  ")
        tempPlaces[index] = UserPlace
        #Get vacation prices from the user and load in the array
        UserPrice = input("Enter the price for the vacation:  ")
        tempPrices[index] = UserPrice

    #return both arrays to main
    return tempPlaces, tempPrices

def PrintArrays(UserPlaces, UserPrices, items):
    #declare local variables
    index = 0

    print("Vacation Spot\t\tVacation Price")
    print("****************************************")
    #print out array
    for index in range(0, items):
          print(UserPlaces[index], "\t\t", UserPrices[index])


     #Non returning function
     #End of function


main()
        









    
