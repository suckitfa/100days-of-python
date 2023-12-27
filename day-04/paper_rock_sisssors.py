import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
your_choice = int(input("What do  you choose?Type 0 for Rock. 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
# print out the ASII
def print_choice(choice_num):
    game_images = [rock,paper,scissors]
    # if choice_num == 0:
    #     print(rock)
    # elif choice_num == 1:
    #     print(paper)
    # else:
    #     print(scissors)
    print(game_images[choice_num])

print_choice(your_choice)
print(f"Computer chose: {computer_choice}")
print_choice(computer_choice)

# all posible choices
# 00 01 02
# 10 11 12
# 20 21 22

# 2 0 1
# 1 2 0
# 0 1 2
if (your_choice == computer_choice):
    print("It is a drawer.")
elif (your_choice == 0 and computer_choice == 1):
    print("Computer wins!")
elif (your_choice == 0 and computer_choice == 2):
    print("You wins!")
elif (your_choice == 1 and computer_choice == 0):
    print("You wins!")
elif (your_choice == 1 and computer_choice == 2):
    print("Computer wins!")
elif (your_choice == 2 and computer_choice == 0):
    print("Computer wins!")
elif (your_choice == 2 and computer_choice == 1):
    print("You wins!")
else:
    print("You typed an invalid number.")