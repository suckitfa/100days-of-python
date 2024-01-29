from turtle import Screen,Turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win?Enter a color:")
# print(user_bet)
colors = ["red","orange","yellow","green","blue","purple"]

all_turtles = []

for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    # tim.forward(100)
    tim.penup() # don't draw
    tim.goto(x=-240,y=-100 + turtle_index * 40)
    all_turtles.append(tim)
print(all_turtles)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
    
def move_forwards():
     tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

screen.listen()
screen.onkey(move_forwards,'w')
screen.onkey(move_backwards,'s')
screen.onkey(turn_left,'a')
screen.onkey(turn_right,'d')

# screen.onkey(key="w", fun)
# screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()