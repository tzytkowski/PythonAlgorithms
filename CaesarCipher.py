def encryptstr(message):
    # Declare local variables
    one_letter = str()
    ascii_letter_value = int()
    new_ascii_value = int()
    new_string = str()
    #Loop to assign new ASCII value
    for index in range(0, len(message)):
        # Get ASCII value of indexed letter
        one_letter = message[index]
        ascii_letter_value = ord(one_letter)
        # Check to see if the letter is z or Z
        # and, if so, assign new value to a or A
        if ascii_letter_value == 122:
            new_ascii_value = 97        
        elif ascii_letter_value == 90:
            new_ascii_value = 65     
        else:        # New value for all others
            new_ascii_value = ascii_letter_value + 1
        # Add the letter to the new string
        new_string = new_string + chr(new_ascii_value)
    return new_string

def decryptstr(message):
    one_letter = str()
    new_string = str()
    ascii_number = int()
    new_ascii_number = int()
    for index in range(0, len(message)):
        one_letter = message[index]
        ascii_number = ord(one_letter)
        if ascii_number == 97:
            new_ascii_number = 122        # a to z
        elif ascii_number == 65:
            new_ascii_number = 90        # A to Z
        else:        # New value for all others
            new_ascii_number = ascii_number - 1
        # Add the letter to the new string
        new_string = new_string + chr(new_ascii_number)
    return new_string


def main():
    user_input = str()
    user_input = input('Enter a string: ')
    d_or_e = input("Would you like you (e)ncrypt or (d)ecrypt your message? ")
    try:
        d_or_e = d_or_e.lower()
        if d_or_e == 'e':
            encrypt = encryptstr(user_input)
            print(encrypt)
        elif d_or_e == 'd':
            decrypt = decryptstr(user_input)
            print(decrypt)
        else:
            print("Wrong")
    except:
        print("Invalid input. Please try again.")

main()