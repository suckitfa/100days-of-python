'''
Date: 2024-01-20 11:02:55
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-01-20 11:10:05
FilePath: \100days-of-python\day-16\my_turtle.py
'''
# import turtle
from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color('coral')
timmy.forward(100)
my_screeen = Screen()
# print(my_screeen.canvheight)
my_screeen.exitonclick()