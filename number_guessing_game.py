import art
import random


attempts = 0
def difficulty():
    while True:
        difficulty = input("choose a difficulty. Type 'hard','easy' or 'demon': ")  # Asking the user the difficulty
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        elif difficulty == 'demon':
            return 1
        else:
            print("invalid type 'easy' or 'hard'")

keep_playing = True

def lives(num):
    if num == 0:
        print(art.logo3)
        print(f"the number was {random_number}")
        global keep_playing
        keep_playing = False

def calculate(random_number, attempts):
    while keep_playing:
        guess_number = int(input("make a guess: "))
        if guess_number > random_number:
            print("Too high")
            attempts -= 1
            print(f"you have {attempts} lives left")
            lives(attempts)

        elif guess_number < random_number:
            print("Too low")
            attempts -= 1
            print(f"you have {attempts} lives left")
            lives(attempts)

        elif guess_number == random_number:
            print(f"you had {attempts} lives left")
            print(art.logo2)
            break

print(art.logo1)
print("welcome to python Number Guessing game!")
print("I'm thinking of a number between 1 and 10")
random_number = random.randint(1, 10)

attempts = difficulty()
print(f"you have {attempts} lives remaining to guess the number.")

calculate(random_number,attempts)

