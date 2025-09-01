import arts
import random
import game_data



score = 0
while True:
    games_data = game_data.data
    print(arts.logo1)
    rando = random.choice(games_data)
    rando1 = random.choice(games_data)

    print(f"Compare A: {rando['name']}, {rando['description']}, {rando['country']}")

    print(arts.logo2)

    print(f"Compare B: {rando1['name']}, {rando1['description']}, {rando1['country']}")
    print(f"A: {rando['follower_count']}")
    print(f"B: {rando1['follower_count']}")

    compared_value = ''
    if rando['follower_count'] > rando1['follower_count']:
        compared_value = rando['follower_count']
    elif rando['follower_count'] < rando1['follower_count']:
        compared_value = rando1['follower_count']

    #print(compared_value)



    guess = input("Who has more followers? (A/B): ").lower()
    if guess == "a":
            guess = rando['follower_count']
            if guess == compared_value:
                print("you're right")
                score += 1

            else:
                print("you're wrong")
                print(f"you're total score is {score}")
                global keep_playing
                break

    elif guess == 'b':
            guess = rando1['follower_count']
            if guess == compared_value:
                print("you're right")
                score += 1

            else:
                print("you're wrong")
                print(f"you're total score is {score}")
                global keep_playing
                break

