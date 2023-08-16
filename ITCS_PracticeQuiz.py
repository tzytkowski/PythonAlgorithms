# A friend of yours opened a cupcake shop a year ago. She wants you to help her analyze her sales by month by 
# creating a program. This program will allow her to enter 12 months of sales and store those values in an array. 
# The program will determine the average sales, the total of all sales, which month had the highest sale, 
# and which month had the lowest sale.

from itertools import count


def LoadList():
    count = 1
    sales_list = []
    monthly_sale = float()
    while count <= 4:
        monthly_sale = int(input("What was your sales this month? "))
        sales_list.append(monthly_sale)
        count = count + 1
    return sales_list

def DetermineTotal(sales_list):
    total = float()
    for i in range(len(sales_list)):
        total = total + sales_list[i]
    return total

def DetermineAverage(total, sales_list):
    total = DetermineTotal(sales_list)
    average = float()
    average = (total / (len(sales_list))) 
    return average


def FindHighest(sales_list):
    highest = sales_list[0]
    for i in range(len(sales_list)):
        for j in range(0, len(sales_list)):
            if sales_list[j] > highest:
                highest = sales_list[j]
    return highest
    

def FindLowest(sales_list):
    lowest = sales_list[0]
    for i in range(len(sales_list)):
        for j in range(0, len(sales_list)):
            if sales_list[j] < lowest:
                lowest = sales_list[j]
    return lowest


def main():
    sales_list = LoadList()
    print("The monthly sales are:", sales_list)
    total = DetermineTotal(sales_list)
    print("The total is:", total)
    avg = DetermineAverage(total, sales_list)
    print("The average sales is:", avg)
    high = FindHighest(sales_list)
    print("The highest number is:", high)
    low = FindLowest(sales_list)
    print("The lowest number is:", low)

main()