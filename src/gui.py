from tkinter import Canvas
from turtle import Turtle, Screen
from score import Score


class GUI():
    def __init__(self):
        self.is_on = True
        self.screen_setup()
        self.scoreboard_setup()
        self.middle_line_setup()

    def update(self):
        self.screen.update()

    def tracer(self, value):
        self.screen.tracer(value)

    def screen_setup(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.listen()

    def scoreboard_setup(self):
        self.score = Score()

    def middle_line_setup(self):
        line = Turtle()
        line.penup()
        line.hideturtle()
        line.setpos(0, -300)
        line.seth(90)
        line.color("white")
        line.pensize(10)
        while line.ycor() < 300:
            line.pendown()
            line.forward(20)
            line.penup()
            line.forward(20)

    def game_over(self):
        self.score.game_over()
        self.is_on = False
        self.screen.exitonclick()
