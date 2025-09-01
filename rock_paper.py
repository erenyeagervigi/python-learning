import random

options = ["rock", "paper", "scissor"]

print("welcome to rock paper scissor game")

computer_output = random.choice(options)

user_input = int(input("0 for rock, 1 for paper, 2 for scissor: "))
if user_input == 0:
    print("rock")
    if computer_output == "paper":
        print("you lose")
    elif computer_output == "scissor":
        print("you win")

if user_input == 1:
    print("paper")
    if computer_output == "rock":
        print("you win")
    elif computer_output == "scissor":
        print("you lose")

if user_input == 2:
    print("scissor")
    if computer_output == "paper":
        print("you lose")
    elif computer_output == "rock":
        print("you win")

print(user_input)