# Tyler Zytkowski
# Bank or credit union rate

def PickInstitution():
    choice = input('Choose between a bank or a credit union: ')
    choice = choice.upper()
    return choice

def Rates():
    user_choice = ''
    rate = str()
    user_choice = PickInstitution()
    if user_choice == 'bank':
        rate = 0.10
    else user_choice == 'credit union':
        rate = 0.05
    return user_choice

def main():
    final_rate = Rates()
    print(final_choice)

main()


    
