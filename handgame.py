import random

#entering values onto words
words = {"apple", "samsung", "oppo", "vivo", "xioami"}

#creating a dictionary
hangman_art = { 0: ("  ",
                    "  ",
                    "  "),
                1: ("  o   ",
                    "     ",
                    "     "),
                2: ("  o  ",
                    "  |  ",
                    "     "),
                3: ("  o  ",
                    " /|  ",
                    "     "),
                4: ("  o  ",
                    " /|\\",
                    "     "),
                5: ("  o  ",
                    " /|\\",
                    " /   "),
                6: ("  o  ",
                    " /|\\",
                    " / \\")}

# a function to know the number of wrong guesses
def display_man (wrong_guesses):
    pass
# a function to know the hints
def display_hint(hint):
    pass
# a function to display answer
def display_answer():
    pass

def main():
    # one of the answer will be chosen at random from words
    answer = random.choice(words)
    print(answer)

if __name__ == "__main__":
    main()