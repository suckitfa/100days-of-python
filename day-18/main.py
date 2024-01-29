'''
Date: 2024-01-28 17:01:44
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-01-28 17:51:35
FilePath: \100days-of-python\day-18\main.py
'''
from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(90)
# timmy_the_turtle.forward(100)
screen = Screen()

screen.exitonclick()