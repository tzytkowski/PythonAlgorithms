# File: Buggy Test Code
# Created By: Paul Rozek
# Date: 20220221

# Background Story
# Jons Car wash is running a holiday promotion where customers can
# buy discounted car washes. With the promotion, car washes are 30% off
# (70% normal price) on Monday through Thursday.
# Standard rates are $5 for basic, $7 for a plus wash which includes underbody wash,
# and $10 for premium wash which includes underobdy, wax, and a spot free rinse.
# Vans and SUV's pay an additional $1 per wash 
# Generate a program to calculate cost of each advance wash purchase.

# Decomp
#  1. Get wash type and vehicle inforation
#  2. Get day of purchase information
#  3. Calculate cost of washes
#  4. Display results to user

# Inputs:  day of wash, wash type, vehicle type

# Outputs: day of wash, wash type, vehicle type, total cost 

#Import Programs
import sys

# Declare Varibles
WeekdayWash = int() # Day of the week (1=Mon, 2=Tues, 3=Wed, 4=Thurs, 5=Fri, 6=Sat, 7=Sun)
WashType = str()    # 1=basic, 2=plus, 3=premium
VehicleType = str() # car, van, suv, and Truck
BasicCost = 5.00      # constant price for basic wash
PlusCost = 7.00        # constant price for plus wasn
PremCost = 10.00       # constant price for premium wash
SuvAdder = 1.00        # constant price upcharge for truck, van or suv
Promotion = 0.70     # constant 70% price (30% off)

TotalCost = float() # Cost of wash

# Code
WeekdayWash = int(input('What day is purchase made on? Enter 1 for Mon, 2 for Tues, 3 for Wed, 4 for Thurs, 5 for Fri, 6 for Sat, 7 for Sun:  '))
if WeekdayWash > 7 or WeekdayWash < 1:      # Exit if out of range
    sys.exit('Variable entered did not meet input criteria (1-7); System Terminated!  ')
WashType = (input('Please select wash type (basic, plus, premium):  '))
if WashType != 'basic' and WashType != 'plus' and WashType != 'premium':                                  # Exit if out of range
    sys.exit('Variable entered did not meet input criteria (1, 2, or 3); System terminated!  ')
VehicleType = (input('Enter vehicle type (car, van, suv, or truck):  '))
if VehicleType != 'car' and VehicleType != 'van' and VehicleType != 'suv' and VehicleType != 'truck':      # Exit if out of range
    sys.exit('Variable entered did not meet input criteria (car, truck, van or suv); System terminated!  ')

# Calculte cost based on day and wash type selected
if WeekdayWash <= 4 and WeekdayWash >=1:    # Weekday Wash
    if WashType == 'basic':                 # Basic Weekday
        TotalCost = BasicCost * Promotion
    elif WashType == 'plus':                # Plus Weekday
        TotalCost = PlusCost * Promotion
    else:                                   # Premium Weekday
        TotalCost = PremCost * Promotion
else:                                       # Weekend Wash
    if WashType == 'basic':                 # Basic Weekend
        TotalCost = BasicCost 
    elif WashType == 'plus':                # Plus Weekend 
        TotalCost = PlusCost 
    else:                                    # Premium Weekend
        TotalCost = PremCost
#end_if

# Factor in Vehicle type
if VehicleType != 'car':
    TotalCost = (TotalCost + SuvAdder)      # $1 added on for large vehicle
else:
    TotalCost = (TotalCost)                 # $1 not added on
#end_if
    
# Print Total Cost
print()
print()
if WeekdayWash > 4:
    print('Weekend prices in effect.  No discount allocated!')
else:
    print('Congrats, you saved 30% by visiting on a weekday!')
print('The cost for a',WashType,'wash for your',VehicleType,'today will be:  $'+("{:.2f}".format(TotalCost)))
print('Please pay the attendant and have a superb day!')
#end_if
        
