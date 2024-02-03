'''
Date: 2024-02-03 17:59:52
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-02-03 18:07:12
FilePath: \100days-of-python\day-22\scoreboard.py
'''
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.write(self.l_score,align='center',font=('Counter',80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align='center',font=('Counter',80,"normal"))
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align='center',font=('Counter',80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align='center',font=('Counter',80,"normal"))
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()