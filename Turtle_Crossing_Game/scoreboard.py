from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_text()

    def update_text(self):
        self.write(f"Level {self.level}", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_text()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
