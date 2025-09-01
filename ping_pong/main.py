import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from dashed_line import Dashed_line

screen = Screen()
screen.title("pong")
screen.bgcolor("black")
screen.setup(width= 800, height = 600)

screen.tracer(0)
#paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
r_paddle.paddle_move_via_updown()
l_paddle.paddle_move_via_ws()

#score_boards
score = Scoreboard((180,200))
score2 = Scoreboard((-180,200))

#dashed lines to separate
dashed_line = Dashed_line()

screen.tracer(1)
ball = Ball()

game_is_on = True
timm = 0.01
while game_is_on:
    time.sleep(timm)
    ball.move()
    #collusions with walls
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.collusions()

    #collusions with paddle
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.collusino()
        timm = timm/10

    elif ball.xcor() > 400:
        score2.update_score()
        timm = 0.01
        ball.refresh()

    elif ball.xcor() < -400:
        score.update_score()
        timm = 0.01
        ball.refresh()

    elif score.score == 10 and score.score > score2.score:
        game_is_on = False
        score.winner()

    elif score2.score == 10 and score2.score > score.score:
        game_is_on = False
        score2.winner()


    screen.update()


screen.exitonclick()