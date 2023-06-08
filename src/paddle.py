from turtle import Turtle


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__("square", 1000, True)
        self.shapesize(stretch_len=3)
        self.seth(270)
        self.color("white")
        self.penup()

        self.speed(0)
        self.move_speed = 20

    def move_up(self):
        self.backward(self.move_speed)

    def move_down(self):
        self.forward(self.move_speed)
