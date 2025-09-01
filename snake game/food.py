from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rando_x = random.randint(-380, 380)
        rando_y = random.randint(-230, 230)
        self.goto(rando_x, rando_y)
