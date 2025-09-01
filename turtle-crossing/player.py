from turtle import Turtle,Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.speed("slow")

    def move(self):
        def up():
            self.forward(10)

        screen = Screen()
        screen.onkeypress(up, "w")
        screen.onkeypress(up, "Up")
        screen.listen()

    def refresh(self):
        self.goto(STARTING_POSITION)