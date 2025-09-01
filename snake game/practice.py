class Score():
    def __init__(self):
        self.value = 0
        print(f"score = {self.value}")
    def scoress(self, num):
        self.value += 1


score = Score()
score.scoress(3)

