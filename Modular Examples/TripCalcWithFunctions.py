#Trip Calculator using functions


def GetInputs():
    #declare local variables
    getmiles = float()
    getmpg = float()
    getfuelcost = float()
    strgetmiles = str()
    strgetmpg = str()
    strfuelcost = str()

    #Ask user values
    strgetmiles = input("Enter miles:  ")
    getmiles = ValidateNumbers(strgetmiles)
    
    strgetmpg = input("Enter mpg:  ")
    getmpg = ValidateNumbers(strgetmpg)
    
    strfuelcost = input("Enter fuel cost:  ")
    getfuelcost = ValidateNumbers(strfuelcost)

    #Be careful here.  Your return HAS to be the same as the call
    return getmiles, getfuelcost, getmpg

def ValidateNumbers(inputstring):
    #Local variables
    validatednumber = float()
    flag = False

    #Validating string to make sure it is a float
    while flag == False:        
        try:
            validatednumber = float(inputstring)
            print("inside validation loop")
            if validatednumber > 0:
                flag = True
            else:
                inputstring = input("Sorry you did not enter a positive number.  Please try again:  ")
            #end if
        except ValueError:
            inputstring = input("Sorry you did not enter a positive number.  Please try again:  ")
        #end try
    #End loop

    #Since this function needs to return a good number we need to use the return statement
    return validatednumber
def main():
    #Declare local variables
    fuelcost = float()
    mpg = float()
    miles = float()
    gallons = float()
    TotalGallons = float()
    TotalCost = float()

    #Get inputs
    #this shows you how to use a function to get
    #many values
    miles, fuelcost, mpg = GetInputs()






main()
