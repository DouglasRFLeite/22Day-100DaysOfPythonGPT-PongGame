from turtle import Turtle, Screen, TurtleScreen
from gui import GUI
from paddle import Paddle


def main():
    screen = GUI()
    paddle1 = Paddle()
    paddle2 = Paddle()
    screen.update()
    screen.screen.listen()
    screen.screen.onkey(key="Up", fun=paddle1.move_up)
    screen.screen.onkey(key="Down", fun=paddle1.move_down)

    while True:
        screen.update()
    screen.screen.exitonclick()


if __name__ == "__main__":
    main()
