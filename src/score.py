from turtle import Turtle


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__("square", 1000, False)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x=0, y=250)

        self.player_points = 0
        self.enemy_points = 0

        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.player_points}   {self.enemy_points}", align="center",
                   font=('Courier', 30, 'normal'))

    def update_score(self):
        self.points += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(f"Game Over!", align="center",
                   font=('Courier', 30, 'normal'))
        self.setpos(0, -40)
        self.write(f"The final score was: {self.player_points} X {self.enemy_points}", align="center",
                   font=('Courier', 18, 'normal'))
