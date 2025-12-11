import random

# Rock Paper Scissors ASCII Art

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)\n
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)\n
"""
rps_list = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

random_index_for_pc = random.choice(rps_list)

if choice > 2 or choice < 0 :
    print("You made a wrong choice. You Lose")

if choice == 0:
    print(rock)
    if random_index_for_pc == rock:
        print(rock)
        print("Draw")
    elif random_index_for_pc == paper:
        print(paper)
        print("You Lose")
    elif random_index_for_pc == scissors:
        print(scissors)
        print("You Win")
    else: 
        print("Pc made a wrong choice. You Win")
elif choice == 1:
    print(paper)
    if random_index_for_pc == rock:
        print(rock)
        print("You Win")
    elif random_index_for_pc == paper:
        print(paper)
        print("Draw")
    elif random_index_for_pc == scissors:
        print(scissors)
        print("You Lose")
    else: 
        print("Pc made a wrong choice. You Win")
elif choice == 2:
    print(scissors)
    if random_index_for_pc == rock:
        print(rock)
        print("You Lose")
    elif random_index_for_pc == paper:
        print(paper)
        print("You Win")
    elif random_index_for_pc == scissors:
        print(scissors)
        print("Draw")
    else: 
        print("Pc made a wrong choice. You Win")
else:
    print("Game Over")

print("----------- Another way to do this --------------")

computer_choice = random.randint(0,2)
if choice >= 0 and choice <= 2:
    print(rps_list[choice])
    print("Computer chose:\n")
    print(rps_list[computer_choice])

if choice >= 3 or choice < 0:
    print("You typed an invalid number. You Lose!")
elif choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 2 and choice == 2:
    print("You Lose!")
elif computer_choice > choice:
    print("You Lose!")
elif choice > computer_choice:
    print("You Win!")
elif computer_choice == choice:
    print("It's a draw!")
else:
    print("Game Over")