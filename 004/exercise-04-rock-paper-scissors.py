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

choose = int(input("\nType [ 1 ] for rockr , [ 2 ] for paper, [ 3 ] for scissors \n"))

print("\nWhat I chose")
if choose == 1:
    print(rock)
elif choose == 2:
    print(paper)
else:
    print(scissors)

print("Computer chose")
computer_choose = random.randint(1, 3)

if computer_choose == 1:
    print(rock)
elif computer_choose == 2:
    print(paper)
else:
    print(scissors)

if (choose == 1 and computer_choose == 3) or (choose == 3 and computer_choose == 2) or (choose == 2 and computer_choose == 1):
    print ("You win!")
elif (choose == computer_choose):
    print("Play Again? [ Yes ] [ Not ]")
else:
    print("You Lose!")


# 1 rock win scissors 3
# 3 scissors win paper 2
# 2 paper win to rock 1
