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
cars = {
    'USA': {
        'Ford': ['Mustang', 'Taurus', 'Expedition'],
        'Chevy': ['Malibu', 'Impala', 'Corvette'],
        'Dodge': ['Charger', 'Challenger', 'Durango']
    },
    'Japan': {
        'Honda': ['Civic', 'Accord', 'NSX'],
        'Toyota': ['RAV4', 'Camry', 'Supra'],
        'Nissan': ['Altima', 'Maxima', '350Z']
    },
    'Germany': {
        'Volkswagen': ['Jetta', 'Golf', 'Passat'],
        'BMW': ['X5', 'M5', 'M2'],
        'Audi': ['A4', 'TT', 'R8']
    }
}

origin = input("Enter the country of origin (USA, Japan, Germany): ")

if origin in cars:
    print()
    make = input(f"You picked {origin}. Choose a make: {', '.join(cars[origin])} ")
    if make in cars[origin]:
        print()
        models = ', '.join(cars[origin][make])
        model = input(f"Pick a model: {models} ")
        if model in cars[origin][make]:
            print()
            print(f"You picked a {make} {model} from {origin}!")
        else:
            print("Invalid model choice")
    else:
        print("Invalid make")
else:
    print("Invalid country of origin")
        
