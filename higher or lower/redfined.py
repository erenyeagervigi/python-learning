import game_data
import arts
import random

def compare(n1,n2):
    if n1 == "a":
        n1 = rando['follower_count']
        n2 = rando1['follower_count']
        if n1 > n2:
            print("you're right!!")
        else:
            print("you're wrong!!")
    if n2 == "b":
        n1 = rando['follower_count']
        n2 = rando['follower_count']
        if n1 < n2:
            print("you're right!!")
        else:
            print("you're wrong")

def check(n1 , n2):
    if n1 > n2:
        return n1
    elif n2 < n1:
        return n2


games_data = game_data.data
print(arts.logo1)
rando = random.choice(games_data)
rando1 = random.choice(games_data)

print(f"Compare A: {rando["name"]}, {rando['description']}, {rando['country']}")

print(arts.logo2)

print(f"Compare B: {rando1["name"]}, {rando1['description']}, {rando1['country']}")

compared_value = check(rando['follower_count'], rando1['follower_count'])

guess = input("Enter who has more followers? (A/B): ").lower()
compare(guess, compared_value)