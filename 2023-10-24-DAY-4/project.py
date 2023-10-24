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

game = [rock, paper, scissors]
option = int(input("Please choose '0' for rock, '1' for paper, '2' scissor!\n"))

if option <= 2 and option >= 0:
    print(f"You choose : \n{game[option]}")
    computer_option = random.choice(game)
    computer_option_index = game.index(computer_option)
    print(f"Computer choose : \n{computer_option}")
    if option == computer_option_index:
        print("Draw!")
    elif option > 2:
        print("Invalid")
    elif option == 0 and computer_option_index == 2:
        print("You Won!")
    elif option == 1 and computer_option_index == 0:
        print("You Won!")
    elif option == 2 and computer_option_index == 1:
        print("You Won!")
    else:
        print("Computer Won!")
else:
   print("Invalid number!") 
    



