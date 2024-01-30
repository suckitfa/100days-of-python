from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.update_scoreboard()
        self.hideturtle()
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)