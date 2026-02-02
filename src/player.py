from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def go_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.teleport(0, -280)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False