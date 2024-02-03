'''
Date: 2024-02-03 12:22:42
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-02-03 18:08:16
FilePath: \100days-of-python\day-22\main.py
'''
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

ball = Ball()

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

scoreboard = ScoreBoard()

screen.listen()

#listenin
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detectcollisionwith r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # detect R paddle misses
    if ball.xcor() > 380:
        scoreboard.r_point()
        ball.reset_position()

    # detect L paddle misses 
    if ball.xcor() < -380:
        scoreboard.l_point()
        ball.reset_position()

screen.exitonclick()