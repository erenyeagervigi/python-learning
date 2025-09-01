print("***************************")
print("welcome to treasure island")
print("***************************")
print("your mission is to find the treasure")
print("you're at a cross road. Where do you want to go? ")

answer = input("type left or right : ").lower()

if answer == "left" or answer == "l":
    print("you've come to the lake")
    answer1 = input("wanna wait till the boat comes, yes or no: ").lower()
    if answer1 == "yes" or answer1 == "y":
        print("a boat comes and u safely reach the island")
        print("when you reach the island you hear a woman singing")
        answer3 = input("do u wanna follow to the place where the women is singing Y or n: ").lower()
        if answer3 == "yes" or answer3 == "y":
            print("you follow there only to see no one but u receive a map on the ground and you follow it to the mansion near the pound")
            answer4 = input("you are tasked to choose between red, white and black door: (black or red or white) ")
            if answer4 == "black" or answer4 == "b":
                print("you chose the black where u get eaten by a dracula!!")
            elif answer == "red" or answer4 == "r":
                print("you chose red where u get eaten by a python")
            else:
                print("you have chosen the right door and you receive the treasure")
        if answer3 == "no" or answer3 == "n":
            print("you come across a bear where u get killed")
    elif answer1 == "no" or answer1 == "n":
        print("you swim and u get eaten by kraken")

elif answer == "right" or answer == "r":
    print("u go the right where ur encountered with the forest")
    print("when you reach the island you hear a woman singing")
    answer3 = input("do u wanna follow to the place where the women is singing Y or n: ").lower()
    if answer3 == "yes" or answer3 == "y":
        print("you follow there only to see no one but u receive a map on the ground and you follow it to the mansion near the pound")
        answer4 = input("you are tasked to choose between red, white and black door: (black or red or white) ")
        if answer4 == "black" or answer4 == "b":
                    print("you chose the black where u get eaten by a dracula!!")
        elif answer == "red" or answer4 == "r":
                    print("you chose red where u get eaten by a python")
        else:
                    print("you have chosen the right door and you receive the treasure")

else:
    print("invalid input")