import random
def black_jack_game():
    play_again = True
    while play_again:
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_rando_cards = random.choices(cards, k = 2)
        computer_rando_cards = random.choices(cards, k = 2)

        print(f"computer cards: {computer_rando_cards[0]}")
        print(f"user's card: {user_rando_cards[0]}, {user_rando_cards[1]}")

        computer_rando_cards_total = sum(computer_rando_cards)
        user_rando_cards_total = sum(user_rando_cards)

        if user_rando_cards_total > 21 and 11 in user_rando_cards:
            user_rando_cards[user_rando_cards.index(11)] = 1
            user_rando_cards_total = sum(user_rando_cards)

        if computer_rando_cards_total < 17:
            new_computer_rando_cards = random.choice(cards)
            computer_rando_cards.append(new_computer_rando_cards)
            computer_rando_cards_total = sum(computer_rando_cards)
            print("computer has added a new card")

        else:
            pass
        one_more_card = True
        while one_more_card:
            user_one_more_card = input("do you wanna add another card? ").lower()
            if user_one_more_card == "yes" or user_one_more_card == "y":
                new_user_rando_cards = random.choice(cards)
                user_rando_cards.append(new_user_rando_cards)
                user_rando_cards_total = sum(user_rando_cards)
                print("you've added a new card")
                one_more_card = False

            elif user_one_more_card == "no" or user_one_more_card == "n":
                one_more_card = False
            else:
                print("Invalid type 'yes' or 'no'")
                continue
            if user_rando_cards_total > 21:
                if not computer_rando_cards_total > 21:
                    print(f"computer cards = {computer_rando_cards} computer score: {computer_rando_cards_total}")
                    print(f"your cards = {user_rando_cards} your score: {user_rando_cards_total}")
                    print("you lose")
                elif computer_rando_cards_total > 21:
                    print(f"computer cards = {computer_rando_cards} computer score: {computer_rando_cards_total}")
                    print(f"your cards = {user_rando_cards} your score: {user_rando_cards_total}")
                    print("No one wins")

            elif user_rando_cards_total <= 21:

                if user_rando_cards_total < computer_rando_cards_total <= 21:
                    print(f"computer cards = {computer_rando_cards} computer score: {computer_rando_cards_total}")
                    print(f"your cards = {user_rando_cards} your score: {user_rando_cards_total}")
                    print("you lose!!")

                elif user_rando_cards_total > computer_rando_cards_total <= 21:
                    print(f"computer cards = {computer_rando_cards} computer score: {computer_rando_cards_total}")
                    print(f"your cards = {user_rando_cards} your score: {user_rando_cards_total}")
                    print("you win!!")

                elif computer_rando_cards_total > 21:
                    print(f"computer cards = {computer_rando_cards} computer score: {computer_rando_cards_total}")
                    print(f"your cards = {user_rando_cards} your score: {user_rando_cards_total}")
                    print("you win!!")

                elif computer_rando_cards_total  == user_rando_cards_total:
                    print(f"computer cards = {computer_rando_cards} computer score: {computer_rando_cards_total}")
                    print(f"your cards = {user_rando_cards} your score: {user_rando_cards_total}")
                    print("draw!!!")


            check_play_again = True

            while check_play_again:
                play_again_user = input("do you wanna play again? (y/n): ").lower()
                if play_again_user == "yes" or play_again_user == "y":
                    check_play_again = False
                elif play_again_user == "no" or play_again_user == 'no':
                    print("Try again later!!")
                    check_play_again = False
                    play_again = False
                else:
                    print("Invalid type 'yes' or 'no'")
                    continue

print("welcome to python black jack game!!!")
black_jack_game()