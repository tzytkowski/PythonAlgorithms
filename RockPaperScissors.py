# Rock Paper Scissors

import random
import sys
def RPSGame():
    guess = str()
    cpu = str()
    wins = 0
    losses = 0
    tie = 0

    # print("Guess (r)ock, (p)aper, (s)cissors or (q)uit")
    choices = ['rock', 'paper', 'scissors', 'quit']
       
    while wins < 5:
        guess = input("Guess (r)ock, (p)aper, (s)cissors or (q)uit: ")
        guess = guess.lower()
        cpu = choices[random.randint(0, 3)]  
            if guess == 'r' and cpu == 'rock':
                print("Its a tie")
                tie = tie + 1
            elif guess == 'r' and cpu == 'scissors':
                print('Rock wins')
                wins = wins + 1
            elif guess == 'r' and cpu == 'paper':
                print('Paper wins')
                losses = losses + 1
            elif guess == 's' and cpu == 'rock':
                print('Rock beats scissors')
                losses = losses + 1
            elif guess == 's' and cpu == 'scissors':
                print('Its a tie')
                tie = tie + 1
            elif guess == 's' and cpu == 'paper':
                print("Scissors beats paper")
                wins = wins + 1
            elif guess == 'p' and cpu == 'rock':
                print('Rock beats paper. You win')
                wins = wins + 1
            elif guess == 'p' and cpu == 'scissors':
                print('You lose')
                losses = losses + 1
            elif guess == 'p' and cpu == 'paper':
                print('Its a tie')
                tie = tie + 1
       


    

        print("Wins:\t", wins, "\nLosses:\t", losses, "\nTies:\t", tie)



def main():
    
    print(RPSGame())

main()
