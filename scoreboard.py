from turtle import Turtle
ALLIGMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")

        self.start()

    def start(self):
        self.goto(0, 280)
        self.write(f"SCORE: {self.score}", True, align=ALLIGMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.start()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALLIGMENT, font=FONT)
