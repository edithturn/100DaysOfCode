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

print("====== Rock Paper Scissors ======")

# Asking for input to the user
choose = int(input("\nType [ 1 ] for rockr , [ 2 ] for paper, [ 3 ] for scissors \n"))

print("\nWhat I chose")
# Assigning a integer value to a each simbol of the play  [sock = 1 , paper = 2 and scissors = 3], in case user insert a invalid number show a menssage
if choose == 1:
    print(rock)
elif choose == 2:
    print(paper)
elif choose == 3:
    print(scissors)
else:
    print("Invalid Number! Type a number 1, 2 or 3")

# If user choose valid number, then generate a random image for the computer
if choose >= 1 and choose <= 3:
    print("Computer chose")
    computer_choose = random.randint(1, 3)

    if computer_choose == 1:
        print(rock)
    elif computer_choose == 2:
        print(paper)
    else:
        print(scissors)

# Applying the rules of the game

    if (choose == 1 and computer_choose == 3) or (choose == 3 and computer_choose == 2) or (choose == 2 and computer_choose == 1):
        print ("You win!")
    elif (choose == computer_choose):
        print("Play Again? [ Yes ] [ Not ]")
    else:
        print("You Lose!")


# 1 rock win scissors 3
# 3 scissors win paper 2
# 2 paper win to rock 1
