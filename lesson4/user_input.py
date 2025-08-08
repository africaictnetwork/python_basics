import sys
import math
import random
from enum import Enum



class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(RPS(2))
print(RPS.ROCK)
print(RPS["ROCK"])
print(RPS.ROCK.value)
sys.exit()
# value = input("please enter a value:\n")
# print(value)

#this code collects input from a user
player_choice = input("Enter...\n1.Rock\n2.Paper\n3.Scissors\n")
player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("you must enter 1, 2 or 3")

computer_choice = random.choice("123")
computer = int(computer_choice)
print("")
print("You chose" + player_choice + ".")
print("Python chose" + computer_choice + ".")

if player == 1 and computer == 3:
    print("You win")
elif player == 2 and computer ==1:
    print("You win")
elif player == 3 and computer == 2:
    print("You win")
elif player == computer:
    print("Its a tie game")

else:
    print("python wins ")






