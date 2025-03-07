import random
import string

chars = " " + string.digits + string.ascii_letters +string.punctuation
chars = list(chars)

key = chars.copy()

random.shuffle(key)

print(f"key: {key}")
print(f"char: {chars}")

org_mssg = input("enter the message u wanna encrypt: ")
encrypted_text = " "

for text in org_mssg:
    index = chars.index(text)
    encrypted_text += key[index]

print(f"the orginal mmsg {org_mssg}")
print(f"the encrypted mssg {encrypted_text}")

encrypted_text = input("enter the message u wanna dencrypt: ")
org_mssg = " "

for text in encrypted_text:
    index = key.index(text)
    org_mssg += chars[index]

print(f"decrypted mssg {org_mssg}")
