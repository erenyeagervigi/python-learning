import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=600, height=800)

#importing indian map
image = "indian_states.gif"
turtle.addshape(image)
turtle.shape(image)

#getting the data from the csv file
data = pd.read_csv("indian_states_coordinates.csv")
all_states = data.states.to_list()
correct_input = []

#keeping tab of codes
scores = 0
while True:

    #asks the user for input
    user_input = screen.textinput(title=f"{scores}/{len(all_states)}", prompt="enter the state").title()
    if user_input == "Q":
        #printing out the value that the user's have missed to enter
        missing_states = [ i for i in all_states if i not in correct_input]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn_indian.csv", index = False)
        break
    if user_input in all_states and user_input not in correct_input:
        user_inputted = data[data.states == user_input]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(user_inputted.x.item(),user_inputted.y.item())
        t.write(user_input)
        correct_input.append(user_input)
        scores += 1

