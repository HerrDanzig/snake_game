from turtle import Turtle
ALLIGMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        with open("data.txt", mode="r") as score:
            self.high_score = int(score.read())

        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")

        self.start()

    def start(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}"
                   , True, align=ALLIGMENT, font=FONT)

    def update(self):
        self.score += 1
        self.start()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as score:
                score.write(str(self.score))
        self.score = 0
        self.start()
