from turtle import Turtle, Screen

LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.positions = [(0,0), (-20,0), (-40,0) ]
        self.turtles = []
        self.create_snake()


    def create_snake(self):
        for position in self.positions:
            self.add_snake(position)

    def add_snake(self, position):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_snake(self.turtles[-1].position())

    def move(self):
        for pos_num in range(len(self.turtles) -1,0,-1):
            new_x = self.turtles[pos_num -1].xcor()
            new_y = self.turtles[pos_num - 1].ycor()
            self.turtles[pos_num].goto(new_x, new_y)
        self.turtles[0].forward(20)
        self.directions()

    def directions(self):

        def left():
            if self.turtles[0].heading() == RIGHT:
                pass
            else:
                self.turtles[0].setheading(LEFT)

        def right():
            if self.turtles[0].heading() == LEFT:
                pass
            else:
                self.turtles[0].setheading(RIGHT)

        def forward():
            if self.turtles[0].heading() == DOWN:
                pass
            else:
                self.turtles[0].setheading(UP)

        def backward():
            if self.turtles[0].heading() == UP:
                pass
            else:
                self.turtles[0].setheading(DOWN)

        screen = Screen()
        screen.onkey(left, "a")
        screen.onkey(right, "d")
        screen.onkey(forward, "w")
        screen.onkey(backward, "s")
        screen.listen()

    def reset(self):
        for sna in self.turtles:

            sna.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()