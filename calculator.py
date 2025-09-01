import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    '/': divide
}
def calculate():
    continue_calculating = True

    num1 = float(input("Enter the first number: "))

    while continue_calculating:

        num2 = float(input("Enter the second number: "))

        for operands in operations:
            print(operands)
        operation = input("Enter the operation u wanna perform: ")

        result = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        continue_again = input(f"do u wanna continue with {result}?(y/n) and 'q' for quit :").lower()
        if continue_again == "yes" or continue_again == "y":
            num1 = result

        elif continue_again == "no" or continue_again == "n":
            continue_calculating = False
            print("\n"* 30)
            calculate()
        elif continue_again == "q":
            print("Thanks for using the calculator!!")
            continue_calculating = False
print(art.logo)
calculate()

