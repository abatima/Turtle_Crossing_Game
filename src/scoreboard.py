from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.teleport(-300, 250)
        self.color("black")
        self.update_scoreboard(f"Level: {self.level}")

    def update_scoreboard(self, text):
        self.write(text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.update_scoreboard("GAME OVER!")

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard(f"Level: {self.level}")