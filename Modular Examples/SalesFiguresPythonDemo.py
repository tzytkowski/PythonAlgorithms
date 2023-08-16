#Sales Figures Program
#written by:  Betsy Jenaway
#Date:  September 21, 2012

#This program asks the user to enter the names of various sales people
#and their sales figures.  It utilizes functions to populate and bring out
#two parallel arrays

#Define what the program will do
def main():
    #declare variables
    Sales = []
    Person = []
    #Load the Person array
    Person = GetSalesPeople()
    #Load the Sales array
    Sales = GetSales()
    #Print out the sales people with their sales
    PrintPeopleSales(Sales, Person)

#Load the Person Array
def GetSalesPeople():
    #declare local variables
    index = 0
    salesperson = "nothing"
    values = []
    #loop to load the Person array
    for index in range(5):
        salesperson = input("Enter the name of the Sales Person:  ")
        values.append(salesperson)
    #send back populated array to main
    return values

#Load the Sales Array
def GetSales():
    #declare local variables
    index = 0
    salesfigure = 0
    values = []
    #loop to load the Sales array
    for index in range(5):
        salesfigure = float(input("Enter the Sales Figure:  $"))
        values.append(salesfigure)
    #return the populated array to main
    return values

#Print the Person and Sales Arrays
def PrintPeopleSales(Sales, Person):
    #declare local variables
    index = 0
    salesperson = "nothing"
    salesfigure = 0.00
    #loop to unload both arrays
    print("_________________________________________________________")
    for index in range(5):
        salesperson = Person[index]
        salesfigure = Sales[index]
        print("|Sales Person:  ", salesperson, "\t|\tSales Figure:  $", salesfigure,"|")
        print("_________________________________________________________")
        
main()
