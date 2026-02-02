from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.reset_position()

    def go_forward(self):
        new_ycor = self.ycor() + 20
        self.teleport(0, new_ycor)

    def reset_position(self):
        self.penup()
        self.goto(STARTING_POSITION)