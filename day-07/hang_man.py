import random
import  hang_man_art as hangman_art
import hangman_words as hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
chosen_word_len = len(chosen_word)
stages = hangman_art.stages

print(hangman_art.logo)

display = []
for _ in range(chosen_word_len):
    display += '_'

print(f"Choosen word = {chosen_word}")
end_of_game = False
lives = len(stages) - 1

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(chosen_word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if not (guess in display):
        print(f"Your guessing letter is {guess}. It is not in the choosen word, so you loose a life.")
        if (lives == 0):
            end_of_game = True
            if not ('_' in display):
               print('You win!')
            else:
               print("You lose!")
        else:
            lives -= 1
    print(stages[lives])
    print(display)

    if not ('_' in display):
        end_of_game = True
        print("You win!")    
