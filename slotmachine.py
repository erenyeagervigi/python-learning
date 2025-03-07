import random
import time

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range (3)]

def print_row(row):
    print("--------------")
    print(" | ".join(row))
    print("--------------")

def payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 6
        elif row[0] == "🍋":
            return bet * 9
        elif row[0] == "🔔":
            return bet * 15
        elif row[0] == "⭐":
            return bet * 50
    return 0


def main():

    balance = 100
    print("--------------------------------")
    print("welcome!! to python slot machine")
    print("symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("--------------------------------")

    while balance > 0:
        print(f"current balance is ${balance} ")

        bet =  input("Enter your bet amt: ")

        if not bet.isdigit():
            print("Enter only numbers")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue
        elif bet <= 0:
            print("bet should be greater than zero!! ")
            continue

        balance -= bet
        row = spin_row()
        print("spinning....\n")
        print_row(row)

        pay = payout(row, bet)
        if pay > 0:
            print(f"congrats!!! you won: ${pay}")
        else:
            print("you have lost")

        balance += pay

        play_again = input("do you wanna play again: ").upper()

        if not play_again == "Y":
            break
    print(f"game over your balance is ${balance}")
if __name__ == "__main__":
    main()