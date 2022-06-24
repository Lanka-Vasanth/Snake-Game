from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score= {self.score}",align="center",font=("Arial",15,"normal"))
    def plus(self):
        self.clear()
        self.score=self.score+1
        self.write(f"Score= {self.score}",align="center",font=("Arial",15,"normal"))
