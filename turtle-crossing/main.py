import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("crossing game- turtle graphics")

player = Player()
score = Scoreboard()
car = CarManager()

game_is_on = True

timeee = 0.1

while game_is_on:
    time.sleep(timeee)

    #lets the turtle to-move forward
    player.move()

    #checks if the turtle has reached the finish line if so it returns to the starting position
    #and updates the scores
    if player.ycor() >290:
        player.refresh()
        timeee = timeee/5
        score.update_score()

    #generates random cars and makes it move
    car.car_move()
    for cars in car.all_cars:
        if player.distance(cars) < 25:
            score.game_over()
            game_is_on = False

    screen.update()
screen.exitonclick()