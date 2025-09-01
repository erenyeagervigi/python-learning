import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US_States Quiz")

#importing the map
screen.bgpic("blank_states_img.gif")

#importing the csv data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_states = []
states_to_learn = []
scores = 0
game_is_on = True
while scores < 50:
    user_input = screen.textinput(title= f"{scores}/{len(data.state)} states correct", prompt= "enter the name of the state").title()
    if user_input == "Quit":
        #printing out the data which the user have not entered
        for i in all_states:
            if i not in guess_states:
                states_to_learn.append(i)
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv",index = False)
        break

    if user_input in all_states and user_input not in guess_states:
        user_inputted = data[data.state == user_input]
        turtle.speed("fastest")
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(user_inputted.x.item(), user_inputted.y.item())
        turtle.write(user_input)
        scores += 1
        guess_states.append(user_input)



