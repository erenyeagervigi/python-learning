from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def collusions(self):
        self.y_move *= -1

    def collusino(self):
        # self.y_move *= -1
        self.x_move *= -1

    def refresh(self):
        # self.speed("fastest")
        self.teleport(0,0)
        self.x_move *= -1
        self.y_move *= -1