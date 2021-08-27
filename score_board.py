from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial"


class Scoreboard(Turtle):

    # Initialisation of scoreboard
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed = 0.5
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    # Puts the most current score on the screen
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT, 24, "normal"))

    # Increases the score by 1 and clears the old score from screen so score can be updated
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # Game Over has been initialised therefore Game Over is written on screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=(FONT, 24, "normal"))

