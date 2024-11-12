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

game_choices = [rock, paper, scissors]

print("Welcome to Rock , Paper, Scissors Game..!!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice < 0 or user_choice > 2:
    print("You enter an wrong choice")
else:
    computer_choice = random.randint(0, 2)
    print(game_choices[user_choice])
    print("Computer Chose: \n")
    print(game_choices[computer_choice])

    if user_choice == 0 and computer_choice == 0:
        print("It's a Tie.!")
    elif user_choice == 0 and computer_choice == 1:
        print("You Lose.!")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win.!")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win.!")
    elif user_choice == 1 and computer_choice == 1:
        print("It's a Tie.!")
    elif user_choice == 1 and computer_choice == 2:
        print("You Lose.!")
    elif user_choice == 2 and computer_choice == 0:
        print("You Lose.!")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win.!")
    elif user_choice == 2 and computer_choice == 2:
        print("It's a Tie.!")
