'''
Date: 2024-01-13 12:38:05
LastEditors: GuangyuanTang 254202042@qq.com
LastEditTime: 2024-01-13 13:15:24
FilePath: \100days-of-python\day-12\answer.py
'''
import art
import random
print(art.logo)
print("Welcome to the guessing number game.")
print("Guess a number between 1 and 100.")
answer = random.randint(1,100)

HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10

def get_difficulty():
    """return the count of turns depends on the user's mode choice:easy=10,hard=10"""
    level = input("Choose a difficulty.Type 'easy' or 'hard'")
    if level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS
    
def check_answer(answer,guess):
    """check the user's guess with answer"""
    if guess == answer:
        print(f"You are right! The answer is {answer}")
        return True
    elif guess > answer:
        print("Too high!")
        return False
    else:
        print("Too low!")
        return False
def game():
    turns = get_difficulty()
    print(f"You have {turns} attempts remaining to guess.")
    guess = int(input("Make a guess:"))
    is_right = check_answer(answer=answer,guess=guess)
    turns -= 1
    while not is_right and turns > 0:
        print(f"You have {turns} attempts remaining to guess.")
        guess = int(input("Make a guess:"))
        turns -= 1
        is_right = check_answer(answer=answer,guess=guess)
    if turns == 0:
        print("You loose! Your turns is over.GAME Over!")

game()