from turtle import Turtle


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__("square", 1000, True)
        self.shapesize(stretch_len=4)
        self.seth(270)
        self.color("white")
        self.penup()
        self.speed(0)
        self.move_speed = 20

    def move_up(self):
        if self.ycor() <= 255:
            self.backward(self.move_speed)
            return True
        return False

    def move_down(self):
        if self.ycor() >= -250:
            self.forward(self.move_speed)
            return True
        return False
