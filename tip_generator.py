print("Welcome to the tip calculator")
bill = int(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? "
                "10, 12, or 15? $"))
total = bill + tip
number_of_ppl = int(input("how many ppl to split the bill to ? "))
split = round(float(total/number_of_ppl),2)
print(f"Each person shout pay: ${split:0.2f}")
