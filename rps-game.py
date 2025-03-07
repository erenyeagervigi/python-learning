import random

option = ("rock", "paper", "scissor")
is_again = True

while is_again:
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("enter the choice(rock, paper, scissor):  ").lower()

    print(f"player choice: {player}")
    print(f"computer choice: {computer}")

    if player == computer:
        print("Draw")

    elif player == "rock" and computer== "paper":
        print(f"YOU lose!!!")
    elif player == "rock" and computer == "scissor":
        print(f"YOU win!!!")
    elif player == "paper" and computer== "rock":
        print(f"YOU win!!!")
    elif player == "paper" and computer == "scissor":
        print(f"YOU lose!!!")
    elif player == "scissor" and computer== "rock":
        print(f"YOU lose!!!")
    elif player == "scissor" and computer== "paper":
        print(f"YOU win!!!")

    if not input("play again (y/n): ") == "y".lower():
        is_again = False
print("thank-you :)")