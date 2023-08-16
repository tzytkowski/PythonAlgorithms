'''
movies = ''
keepGoing = 'yes'
while keepGoing == 'yes':
    movies = input("Pick a movie: ")
    if movies == 'goodfellas' or movies == 'scarface':
        x = input('Any other mob movies you like? ')
        print(x)
    print("I like that movie too")
    keepGoing = input("Do you want to keep going? ")
'''

'''
Get the number of cars parked in the parking lot.
Add today’s number to yesterday’s number.
Print out the total.
'''


'''
total = 0 
counter = 0

while counter <= 7:
    cars = int(input('How many cars in lot?  '))
    total = cars + total
    counter = counter + 1
    print(total)
'''

'''
How many cookies 
6 or less cookies, no discount
7-12, 5% discount
13-24, 10% discount
Over 25, 20% discount
Keep entering until user says quit
Cookies are .50 each
Calculate subtotal before discount
Output discount and total purchased

Ask how many cookies
Determine discount rate
Determine subtotal
Determine discount amount
Determine total
Output discount, subtotal and total
Ask if the user wants to purchase more cookies
'''
'''
x = float()
discount = 0.00
user = str()
while user != 'quit' or user != 'no':
    x = float(input("How many cookies are you buying?  "))
    if x <= 6:
        discount = 0.00
    elif x >= 7 and x <= 12:
        discount = 0.05
    elif x >= 13 and x <= 24:
        discount = 0.10
    elif x >= 25:
        discount = 0.20
    else:
        print("Invalid code")
    subtotal = x * 0.50
    discountAmount = subtotal * discount
    total = subtotal - discountAmount
    print("Subtotal is: ", format(subtotal, '.2f'))
    print("The discount amount is: ", format(discountAmount, '.2f'))
    print("The total is: ", format(total, '.2f'))
    user = input("Would you like to buy more cookies? ")
'''
'''
counter = 0
second = int(input('How many seconds have passed? '))
minute = 0
hour = 0

while second == 60:
    second = second + 1
    while minute == 60:
        minute = minute + 1
        hour = hour + 1
        counter = counter + 1
print(minute)
'''
'''
total = 0
count = 1
while total < 100:
    x = int(input("Number: "))
    total = total + x
    count = count + 1
print(total)
'''

weeks = int(input("Weeks: "))
sales = int(input("Sales: "))
total_sales = int()
avg_sales = int()

for i in range(weeks):
  total_sales = total_sales + sales
  avg_sales = total_sales / weeks
  print("Total sales: ",total_sales)
  print("Average sales: ", avg_sales)
