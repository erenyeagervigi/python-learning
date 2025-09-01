letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("welcome to the ceaser cipher python!!!")

def encrypt(texts, number):
    encrypted_list = []
    for text in texts:
        indexs = 0
        indexs += letters.index(text)
        if indexs >= 25:
            indexs = -1

        encrypted_list.append(letters[indexs + number])
    listtt = ""
    for data in encrypted_list:
        listtt += data
    print(f"your encrypted mssg is '{listtt}'")
def decrypt(texts, number):
    encrypted_list = []
    for text in texts:
        indexs = 0
        indexs += letters.index(text)
        if indexs >= 25:
            indexs = 0

        encrypted_list.append(letters[indexs - number])
    listtt = ""
    for data in encrypted_list:
        listtt += data
    print(f"decrypted message is '{listtt}'")

user_input = input("Type 'e' to encrypt and d to 'decrypt: ").lower()
user_mssg = input("Type your message: ").lower()
user_shift = int(input("type the number u wanna shift it to: "))
if user_input == "e":
    encrypt(user_mssg, user_shift)
elif user_input == "d":
    decrypt(user_mssg, user_shift)