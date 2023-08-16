#Examples of Mutable and Immuatable objects

#Global Variables
a_name = str()
#giving a_name a value
a_name = 'Sue'

def ChangeName():
    #local variables
    a_name = str()
    #changing the value of a_name
    a_name = 'Bob'
    #printing a_name
    print("Inside ChangeName, a_name = ", a_name)

def main():
    #main's variables
    a_name = str()
    #calling ChangeName
    ChangeName()
    #printing a_name inside main()
    print("Inside main() after ChangeName is called, a_name = ", a_name)
    #Changing a_name in main()
    a_name = 'John'
    print("Inside main() after a_name is changed, a_name = ", a_name)

main()
#printing a_name in global
print("Outside all functions, a_name = ", a_name)
    
