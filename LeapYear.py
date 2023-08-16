def leapyear():
    flag = 0
    year = input('Enter a year: ')
    year = int(year)
    try:
        while True:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print(year, "is a leap year!")
            elif year % 4 != 0:
                print("{1} Not a leap year" .format(year))
            elif year % 100 != 0:
                print("{0} is not a leap year")
            elif year % 400 != 0:
                print(year, " is not a leap year")
            
    except:
        print("You did not enter a valid number")

x = leapyear()
print(x)