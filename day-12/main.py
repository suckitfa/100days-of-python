import art
import random
print(art.logo)
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

answer = random.randint(1,100)

def get_turns():
    turns = 10
    mode = input("Choose your mode: easy or hard. default:easy")
    if mode == 'hard':
        turns = 5
    return turns

def user_guess():
    guess_num = int(input("guess a number from 1 to 100:"))
    if guess_num < 1 or guess_num > 100:
        print("Guess number out of range")
    if answer == guess_num:
        print('You are right!')
        return True
    elif answer > guess_num:
        print("Too lower")
        return False
    else:
        print("Too high")
        return False

turns = get_turns()
while turns > 0:
    is_right = user_guess()
    if is_right:
        break
    turns -= 1