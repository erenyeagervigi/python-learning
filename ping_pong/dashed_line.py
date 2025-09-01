from turtle import Turtle

class Dashed_line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.setheading(270)
        self.penup()
        self.goto(0,300)
        self.pensize(5)
        self.line()

    def line(self):
        for i in range(50):
            self.penup()
            self.forward(17)
            self.pendown()
            self.forward(10)
