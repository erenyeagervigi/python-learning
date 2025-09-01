print("welcome to python pizza!!")
size = input("what size pizza do you want? S, M or L : ").lower()

total = 0

if size == "small" or size == "s":
    total += 15
elif size == "medium" or size == "m":
    total += 20
elif size == "large" or size == "l":
    total += 25

pepperoni =input("Do you want pepperoni on your pizza? Y or N : ").lower()

if pepperoni == "yes" or pepperoni == "y":
    if size == "small":
        total += 2
    else:
        total += 3

if pepperoni == "no" or pepperoni == "n":
    pass

extra_chess = input("Do you want extra chesse? Y or N : ").lower()
if extra_chess == "yes" or extra_chess == "y":
    total += 1
elif extra_chess == "no" or extra_chess == "n":
    pass

print(f"Your total is ${total}")