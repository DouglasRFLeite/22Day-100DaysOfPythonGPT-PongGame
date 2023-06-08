from turtle import Turtle
from paddle import Paddle

UP = 0
DOWN = 1


class Enemy(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.setpos(270, 0)
        self.move_speed = 1
        self.direction = UP

    def move(self):
        if self.direction == UP:
            if not self.move_up():
                self.direction = DOWN
        else:
            if not self.move_down():
                self.direction = UP
