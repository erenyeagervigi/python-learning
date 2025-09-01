import random
import word_lists
word_list = word_lists.word_list
hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]
print("welcome to python hangman!!")
rando_word = random.choice(word_list)
#print(rando_word)

wordlen = len(rando_word)

placeholder = ""
for i in range(0,wordlen):
    placeholder += "_"
print(placeholder)

game_over = False
corrected_letters = []

lives = 0

while not game_over:
    user_guess = input("Enter your guess: ").lower()

    display = " "


    for word in rando_word:

        if word == user_guess:
            display += word
            corrected_letters.append(word)

        elif word in corrected_letters:
            display += word
        else:
            display += '_'
    print(display)

    if user_guess not  in rando_word:
        lives += 1

        if lives == 6:
            print("game over")
            game_over = True

    if "_" not in display:
        game_over = True
        print("you win")

    print(hangman_stages[lives])