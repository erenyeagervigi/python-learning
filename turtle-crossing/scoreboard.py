from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-250, 250)
        self.write(f"score: {self.score}",font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.goto(-50,0)
        self.write("Game Over",font=FONT)
