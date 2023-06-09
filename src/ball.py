from turtle import Turtle
from paddle import Paddle
import random
import numpy as np


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__("circle", 1000, True)
        self.seth(random.randint(0, 360))
        self.penup()
        self.color("white")

        self.move_speed = 1

    def reset(self):
        self.setpos(0, 0)
        self.seth(random.randint(0, 360))

    def move(self):
        self.forward(self.move_speed)
        if self.ycor() > 280 or self.ycor() < -280:
            self.seth(360-self.heading())

    def hits(self, paddle: Paddle) -> bool:
        if self.distance(paddle) < 20:
            return True
        elif np.abs(self.xcor()) > (np.abs(paddle.xcor()) - 15) and self.distance(paddle) < 60:
            return True
        else:
            return False

    def bounce(self):
        self.seth(180-self.heading())
