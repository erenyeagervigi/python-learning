import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


symbols = ['!', '@', '#', '$','&', '*', '-','~']

print("welcome to password generator!!!")
size = int(input("Enter the size of the password you wanna generate: "))


how_many_letters = round(size * 0.7)
how_many_numbers = round(size * 0.2)
how_many_symbols = size - (how_many_letters + how_many_numbers)

password = ""

for char in range(0, how_many_letters):
    password += random.choice(letters)

for char in range(0, how_many_numbers):
    password += random.choice(numbers)

for char in range(0, how_many_symbols):
    password += random.choice(symbols)

print(f"The password generated is {password}")