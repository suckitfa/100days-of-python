'''
Date: 2024-01-30 09:12:33
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-02-18 09:27:02
FilePath: \100days-of-python\day-24\snake-game\scoreboard.py
'''
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # init high_score from file
        self.high_score = 0
        with open('data.txt') as f:
            self.high_score = int(f.read())
            f.close()
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.update_scoreboard()
        self.hideturtle()
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as f:
                f.write(str(self.high_score))
                f.close()
        self.score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score}, High Score {self.high_score}", align=ALIGNMENT, font=FONT)