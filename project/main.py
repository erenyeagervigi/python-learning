import random
from turtle import Turtle, Screen




screen = Screen()
screen.setup(width = 800, height =500)
user_input = screen.textinput(title="make a bet", prompt= "enter the you're bet turtle")
screen.bgcolor("black")
t = Turtle()
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

def shapeee(n):
    n.shape("turtle")

def penupp(n):
    n.penup()
    shapeee(n)

objects = [t1,t2,t3,t,t4,t5,t6]

colours = ["red", "orange", "yellow", "green", "blue", "violet", "indigo"]

for i, turtle in enumerate(objects):
    turtle.color(colours[i])


for i in objects:
    penupp(i)

is_race_on = False

if user_input:
    is_race_on = True

places = [150,100,50,0,-50,-100,-150]
for i, turtle in enumerate(objects):
    turtle.speed("normal")
    turtle.goto(-380, places[i])

while is_race_on:
    for i in objects:
        if i.xcor() >= 380:
            print(f"the winner is :{i.pencolor()}")
            if user_input == i.pencolor():
                print("you've won")
            else:
                print("you've lost")
            is_race_on = False
        if user_input == i.pencolor(): #cheat
            if i.xcor() >= 200:
                i.forward(100)


        speed = random.randint(0, 10)
        i.forward(speed)


screen.exitonclick()