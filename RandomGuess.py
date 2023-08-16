import random
import sys

def RandomGuess():
    guess = int()
    number = int()
    guess_amount = 1
    number = random.randint(1, 100)
    print('I am thinking of a number between 1-100')
    while guess_amount < 4:
        guess = int(input('Take a guess: '))
        if guess == number:
            print("Congratulations! ", guess, ' is the right number!')
            break
        elif guess > number:
            print('Too high')
            guess_amount = guess_amount + 1
            continue
        elif guess < number:
            print('Too low')
            guess_amount = guess_amount + 1
            continue
        elif guess != number:
            print('Wrong number!')
            guess_amount = guess_amount + 1
            continue
        else:
            print("I'm a little confused")
            guess_amount = guess_amount + 1
            continue
    if guess_amount == 3:
        sys.exit("You have run out of guesses. Thank you for playing!")


        

def main():
    print(RandomGuess())

main()
