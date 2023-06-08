from turtle import Turtle
from paddle import Paddle


class Player(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.setpos(-270, 0)
