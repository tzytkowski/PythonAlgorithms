def main():
  new = AddNumbers()
  print(new)


def GetNumbers():
  strNumber = ""
  strNumber2 = ""
  number = int()
  number2 = int()
  flag = 0
  while flag == 0:
    strNumber = input("Enter a number: ")
    try:
      number = int(strNumber)
      flag = 1
    except:
      print("Cant convert. Try again")
      continue
  while flag == 1:
    strNumber2 = input('Enter another number: ')
    try:
      number2 = int(strNumber2)
      flag = 2
    except:
      print("Cant convert number 2. Try again")
      continue
  print('Numbers are ', number, ' and ', number2)
  return number, number2

def AddNumbers():
  x, y = GetNumbers()
  sum = x + y
  return sum


main()
  