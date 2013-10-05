import random
import time

play = 'y'
victories = 0
losses = 0
ties = 0

while play == 'y':

    print("In all lowercase letters, ")
    pChoice = input("please type rock, paper, or scissors: ")
    cpuChoice = random.randint(1,3)

    print("Rock!")
    time.sleep(0.5)
    print("Paper!")
    time.sleep(0.5)
    print("Scissors!")
    time.sleep(0.5)

    if pChoice == "rock" and cpuChoice == 1:
          win = 'tie'
    elif pChoice == 'rock' and cpuChoice == 2:
          win = 'lose'
    elif pChoice == 'rock' and cpuChoice == 3:
          win = 'win'
    elif pChoice == 'paper' and cpuChoice == 1:
          win = 'win'
    elif pChoice == 'paper' and cpuChoice == 2:
          win = 'tie'
    elif pChoice == 'paper' and cpuChoice == 3:
          win = 'lose'
    elif pChoice == 'scissors' and cpuChoice == 1:
          win = 'lose'
    elif pChoice == 'scissors' and cpuChoice ==2:
          win = 'win'
    elif pChoice == 'scissors' and cpuChoice == 3:
          win = 'tie'
    else:
        print("Invalid hand usage.\n")
        continue

    if cpuChoice == 1:
        cpuChoice = 'rock'
    elif cpuChoice == 2:
        cpuChoice = 'paper'
    elif cpuChoice == 3:
        cpuChoice = 'scissors'


    print("\nYou chose " + pChoice + ".")
    print("The computer chose " + cpuChoice + ".\n")
    print("You " + win + "!\n")

    time.sleep(3)

    if win == 'win':
        victories += 1
    elif win == 'lose':
        losses += 1
    elif win == 'tie':
        ties += 1
    print("You have won " + str(victories) + ' times')
    print('You have lost ' + str(losses) + ' times')
    print('You have tied ' + str(ties) + ' times')
    play = input("Play again? (y/n) ")

