print("welcome to python bidding!!!")
bid = {}

def find_highest_bidder(name, amout):
    highest_bid = 0
    winner = ''
    for bidder in bid:
        bidder_amt = bid[bidder]
        if bidder_amt > highest_bid:
            highest_bid = bidder_amt
            winner = bidder

    print(f"the winner is {winner} with an amount of {highest_bid}")
check_continue = True
while check_continue:
    name = input("Enter your name: ")
    price = int(input("Enter your bidding amount: $"))
    bid[name] = price
    should_continue = input("Are there any other bidders: ").lower()
    if should_continue == "no" or should_continue == "n":
        find_highest_bidder(name, price)
        check_continue = False
    elif should_continue == "yes" or should_continue == "y":
        print("\n" * 20)

