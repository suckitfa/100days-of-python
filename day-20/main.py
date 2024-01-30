'''
Date: 2024-01-29 22:03:17
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-01-30 10:04:56
FilePath: \100days-of-python\day-20\main.py
'''
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 15:
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()