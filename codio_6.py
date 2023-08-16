'''
x = int()
i = int()
# j = int()

x = int(input('Number: '))
for i in range(1, x+1):     # 1, 2, 3, 4, 5
    for j in range(5, 0, -1):  # 
      print('.' * j, end = '')
    print(i)
'''



# Decomposition
# Ask number of wings they want
# Ask for type of sauce


# Inputs
# Number of wings
# Sauce

# Outputs
# Total price


wings = int()
sauce = ""
price = float()
discount = float()
total = float()
subtotal = float()
user = ""

while user != 'Q':
sauce = input("Type: ")
print()
wings = int(input("Quantity: "))
if sauce == 'hot' and wings <= 6:
    discount = 0.0
elif sauce == 'hot' and (wings > 6 and  wings<= 12):
    discount = -0.10
elif sauce == 'hot' and (wings > 12 and wings <= 24):
    discount = 0.20
elif sauce == 'sour' and wings <= 6:
    discount = 0.05
elif sauce == 'sour' and (wings > 6 and wings <= 12):
    discount = 0.10
elif sauce == 'sour' and (wings > 12 and wings <= 24):
    discount = 0.15
elif wings > 24:
discount = 0.25

price = 0.50

subtotal = price * wings

total = subtotal - (wings * discount) 
print()
print('Total:', total)
user = input('Continue: ') 
print()


