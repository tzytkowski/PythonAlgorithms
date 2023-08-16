list = [2, 11, 88, 9, 22, 8]
highest = list[0]
for j in range(0, len(list)-1):
    if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
print(list)
print(highest)