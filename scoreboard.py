from turtle import *

ALIGNIMENT = "center"
FONT = ("Ariel", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.upgrade_scoreboard()

    def upgrade_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNIMENT,font=FONT )

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER! \n\nyour score: {self.score}", align=ALIGNIMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.upgrade_scoreboard()