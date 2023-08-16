def GetBugs():
    amount = int()
    list = []
    for i in range(0, 7):
        amount = input("How many bugs did you collect this week? ")
        list.append(amount)  
    return list

def GetSubtotal(list):
    list = GetBugs()
    for i in list:
        subtotal += list[i]
    print(subtotal)

def GetTotal(subtotal):
    subtotal = GetSubtotal(list)
    user = input("Would you like to calculate your bugs? ")
    user = user.lower()
    while user != "no":
        total += subtotal
        user = input("Keep going? ")
    return total


def main():
    total = int()
    x = 1
    list = GetBugs()
    print(list)
    GetSubtotal(list)
    total = GetTotal(subtotal)
    print("The total is", total)


main()
