import time
from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("python snake game")
screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 20:
        snake.extend()
        food.refresh()
        scoreboard.scores()

    if snake.turtles[0].xcor() > 390 or snake.turtles[0].xcor() < -390 or snake.turtles[0].ycor() > 240 or snake.turtles[0].ycor() < -240:
        scoreboard.reset()
        snake.reset()

    for snakes in snake.turtles[1:]:
        if snake.turtles[0].distance(snakes) < 10:
            scoreboard.reset()
            snake.reset()

screen.delay(1)
screen.exitonclick()