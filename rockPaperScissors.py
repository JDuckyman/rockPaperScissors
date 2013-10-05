import random
import time

play = 'y'

while play == 'y':

    print("In all lowecase letters, ")
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

    if cpuChoice == 1:
        cpuChoice = 'rock'
    elif cpuChoice == 2:
        cpuChoice = 'paper'
    elif cpuChoice == 3:
        cpuChoice = 'scissors'


    print("You chose " + pChoice + ".")
    print("The computer chose " + cpuChoice + ".")
    print("You " + win + "!")

    time.sleep(3)

    play = input("Play again? (y/n) ")

