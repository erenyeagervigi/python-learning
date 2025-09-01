from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.highscore =  file.read()
        self.highscore = int(self.highscore)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.write(f"Score: {self.score}    High score: {self.highscore}", align="center", font=('Arial', 16, 'normal'))

    def scores(self):
        self.score += 1
        self.update_scores()

    # def game_over(self):
    #     self.color("red")
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align="center", font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt",'w') as file:
                file.write(f"{str(self.score)}")
        self.score = 0
        self.update_scores()