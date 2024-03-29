'''
Date: 2024-02-03 13:11:56
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-02-03 18:19:18
FilePath: \100days-of-python\day-22\ball.py
'''
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("red")
        self.penup()
        # the speed of the ball
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()