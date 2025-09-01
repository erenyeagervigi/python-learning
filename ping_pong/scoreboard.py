from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.coordinate = coordinate
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(coordinate)
        self.scoress()
    def scoress(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=('Arial', 50, 'normal'))

    def update_score(self):
        self.score += 1
        self.scoress()

    def winner(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"game over!!", align="center", font=('Arial', 45, 'normal'))