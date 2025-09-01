import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_words = {item.letter: item.code for index,item in data.iterrows()}

while True:
    user_input = input("Enter your fav anime char: ").upper()
    try:
        output = [phonetic_words[_] for _ in user_input]
    except KeyError:
        print("please enter valid alphabets")
    else:
        print(output)
        break