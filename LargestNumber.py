message = input("Message: ")
new = []
for index in range(0, len(message)):
    one_letter = message[index]
    new.append(one_letter)
    new_index = ord(one_letter)

print(new)
print(new_index)
