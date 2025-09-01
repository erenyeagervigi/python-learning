import turtle
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)


    def paddle_move_via_ws(self):
        screen = turtle.Screen()
        def forward():
            y_pos = self.ycor() + 20
            self.goto(self.xcor(), y_pos)
        def backward():
            y_pos = self.ycor() - 20
            self.goto(self.xcor(), y_pos)

        screen.onkeypress(forward, "w")
        screen.onkeypress(backward, "s")
        screen.listen()

    def paddle_move_via_updown(self):
        screen = turtle.Screen()
        def forward():
            y_pos = self.ycor() + 10
            self.goto(self.xcor(), y_pos)
        def backward():
            y_pos = self.ycor() - 10
            self.goto(self.xcor(), y_pos)

        screen.onkeypress(forward, "Up")
        screen.onkeypress(backward, "Down")
        screen.listen()