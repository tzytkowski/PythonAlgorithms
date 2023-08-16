def StudentGrades():
    try:
        data = False
        while data == False:
            test1 = input("1: ")
            try:
                test1 = int(test1)
            except:
                print('Invalid. Try again')
                continue
            if test1 > 100 or test1 < 0:
                print('Try again')
                continue
            else:
                data = True
        data = False
        while data == False:
            test2 = input("2: ")
            try:
                test2 = int(test2)
            except:
                print('Invalid. Try again')
                continue
            if test2 > 100 or test2 < 0:
                print('Try again')
                continue
            else:
                data = True
        data = False
        while data == False:
            test3 = input("3: ")
            try:
                test3 = int(test3)
            except:
                print("Only numbers. Try again")
                continue
            if test3 > 100 or test3 < 0:
                print('Try again')
                continue
            else:
                data = True
        average = (test1 + test2 + test3) / 3
        return format(average, '.2f')
    except:
        print("Invalid")

x = StudentGrades()
print(x)

