from turtle import Turtle, Screen, TurtleScreen
from gui import GUI
from paddle import Paddle
from player import Player
from enemy import Enemy
from ball import Ball
import time


def main():
    screen = GUI()
    player = Player()
    enemy = Enemy()
    ball = Ball()
    screen.update()

    screen.screen.onkey(key="Up", fun=player.move_up)
    screen.screen.onkey(key="Down", fun=player.move_down)
    screen.screen.onkey(key="x", fun=screen.game_over)

    while screen.is_on:
        time.sleep(0.004)
        enemy.move()
        ball.move()

        # Detect colision:
        if ball.hits(player) or ball.hits(enemy):
            ball.bounce()

        # Detect point:
        if ball.xcor() < -300:
            ball.reset()
            screen.score.enemy_scores()
        elif ball.xcor() > 300:
            ball.reset()
            screen.score.player_socres()

        screen.update()


if __name__ == "__main__":
    main()
