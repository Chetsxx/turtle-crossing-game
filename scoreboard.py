from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.goto(-200, 250)
        self.write(f"LEVEL {self.level}", False, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!!!\nYOUR SCORE: {self.level}", False, align="center", font=FONT)
