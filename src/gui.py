from tkinter import Canvas
from turtle import Turtle, Screen


class GUI():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

    def update(self):
        self.screen.update()
