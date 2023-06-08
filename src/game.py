from turtle import Turtle, Screen, TurtleScreen
from gui import GUI
from paddle import Paddle
from player import Player
from enemy import Enemy
import time


def main():
    screen = GUI()
    player = Player()
    enemy = Enemy()
    screen.update()

    screen.screen.onkey(key="Up", fun=player.move_up)
    screen.screen.onkey(key="Down", fun=player.move_down)
    screen.screen.onkey(key="x", fun=screen.screen.bye)

    while True:
        time.sleep(0.002)
        enemy.move()
        screen.update()
    screen.screen.exitonclick()


if __name__ == "__main__":
    main()
