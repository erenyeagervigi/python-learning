from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []

    def make_car(self):
        x = random.randint(1,6)
        if x == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(random.randint(300,400), random.randint(-280,300))
            self.all_cars.append(new_car)


    def car_move(self):
        self.make_car()
        for cars in self.all_cars:
            cars.forward(STARTING_MOVE_DISTANCE)

