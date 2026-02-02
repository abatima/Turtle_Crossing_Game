from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-300, 250)
        self.color("black")
        self.update_scoreboard(f"Level: {self.score}")

    def update_scoreboard(self, text):
        self.write(text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.update_scoreboard("GAME OVER!")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard(f"Level: {self.score}")