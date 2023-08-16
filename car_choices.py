# Tyler Zytkowski
# 2/22/2022
'''
This program asks which country you want a car from,
    what make you'd like, and ultimately which model you'd like it to be.
    After gathering that information, it tells you the exact car you picked.
'''

# Ask user which country they would like their car from
# Ask user which car make they would like
# Ask user which car model they would like
# Determine exactly what car they want

# Inputs
# Country of origin
# Make of car
# Model of car

# Outputs
# Type of car desired

import sys

# Delcare variables
origin = str()
make = str()
model = str()

# Get input to decide what country user wants car from 
origin = int(input("What country do you want your car from? USA, Japan or Germany: "))


if origin == 'USA':            
    make = input('You picked USA. Do you want a Ford, Chevy or Chrysler? ')
    if make == 'Ford':
        make = 'Ford'   
        model = input('Pick a Mustang, Taurus or Expedition: ')
        if model == 'Mustang':
            model = 'Mustang'
        elif model == 'Taurus':
            model = 'Taurus'
        elif model == 'Expedition':
            model = 'Expedition'
        else:
            print('Invalid model')
    elif make == 'Chevy':
        make = 'Chevy'
        model = input('Pick a Malibu, Impala or Corvette: ')
        if model == 'Malibu':
            model = 'Malibu'
        elif model == 'Impala':
            model = 'Impala'
        elif model == 'Corvette':
            model = 'Corvette'
        else:
            print('Invalid model choice')
    elif make == 'Doge':
        make = 'Dodge'
        model = input('Pick a Charger, Challenger or Durango: ')
        if model == 'Charger':
            model = 'Charger'
        elif model == 'Challenger':
            model = 'Challenger'
        elif model == 'Durango':
            model = 'Durango'
        else:
            print('Invalid model choice')

    else:
        print('Invalid choice')
elif origin == 'Japan':
    print()
    make = input('You picked Japan. Would you like a Honda, Toyota or Nissan? ')
    print()
    if make == 'Honda':
        model = input('Pick a Civic, Accord or NSX: ')
        if model == 'Civic':
            model = 'Civic'
        elif model == 'Accord':
            model = 'Accord'
        elif model == 'NSX':
            model = 'NSX'
        else:
            print('Invalid model')
    elif make == 'Toyota':
        make = 'Toyota'
        model = input('You picked Toyota. Would you like a RAV4, Camry or Supra? ')
        if model == 'RAV4':
            model = 'RAV4'
        elif model == 'Camry':
            model = 'Camry'
        elif model == 'Supra':
            model = 'Supra'
    elif make == 'Nissan':
        make = 'Nissan'
        model = input('Would like you like an Altima, Maxima or 350Z? ')
        if model == 'Altima':
            model = 'Altima'
        elif model == 'Maxima':
            model = 'Maxima'
        elif model == '350Z':
            model = '350Z'
        else:
            print('Invalid model choice')
    else:
        print("Too soon Junior. Invalid choice")

elif origin == 'Germany':
    print()
    make = input('You picked Germany. Would you like a Volkwagen, Audi or BMW? ')
    print()
    if make == 'Volkswagen':
        make = 'Volkswagen'
        model = int(input('You picked Volkswagen. Would you like a Jetta, Golf or Passat? '))
        if model == 'Jetta':
            model = 'Jetta'
        elif model == 'Golf':
            model = 'Golf'
        elif model == 'Passat':
            model = 'Passat'
        else:
            print('Invalid model')
    elif make == 'BMW':
        make = 'BMW'
        model = input('You picked BMW. Would you like an X5, M5 or M2? ')
        if model == 'X5':
            model = 'X5'
        elif model ==- 'M5':
            model = 'M5'
        elif model == 'M2':
            model ='M2'
        else:
            print('Invalid model')
    elif make == 'Audi':
        make = 'Audi'
        model = input('Would you like a A4, TT or R8? ')
        if model == 'A4':
            model = 'A4'
        elif model == 'TT':
            model = 'TT'
        elif model == 'R8':
            model = 'R8'
        else:
            print('Invalid choice')
    else:
        print('Invalid choice')
else:
    print()
    print("No valid country of origin selected ---- Program Terminated")
    print()


print()
print('You picked a', make, model, 'from', origin + '!')
print()
        