def show_balance():
     print(f"your balance is ${balance}")
def deposit():
    amount = int(input("Enter the amount you wanna enter: $"))
    if amount < 0:
        print("not valid")
        return 0
    else:
        return amount
def withdraw():
    amount = int(input("Enter the amount you wanna withdraw: $"))

    if amount > balance:
        print("balance is not available ")
    elif amount <= balance:
        return amount

balance = 0
is_running = True

while is_running:
    print("WELCOME")
    print("1. show-balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. EXIT")

    choice = input("ENTER THE THING YOU WANNA DO: ")
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("That is not valid!!")

print("THANK YOU HAVE A NICE DAY!!!")