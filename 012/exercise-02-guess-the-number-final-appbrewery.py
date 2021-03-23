import art
import random

print(art.logo)

EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 10
print("Welcome to the Number Guessing Game!")
print("I am thinking a number betweek 1 and 100")

# variables
num = random.randint(1, 100)

def Game():
    """Calculate the number of attemps"""
    difficulty = input(f"Choose a difficulty. Type [ easy ] or [ hard ] : ")
    if difficulty.lower() == "easy":
        return EASY_LEVEL_TURNS            
    elif difficulty.lower() == "hard":
        return HARD_LEVEL_TURNS

def Guessing():
    keep_guessing = True
    attemp = Game()
    
    print(f"Number {num}")
       
    while keep_guessing:
        guess_number = int(input(f"Make a guess : "))
       
        if guess_number > num:
            print("Too High")
            attemp -= 1
            keep_guessing = True
        elif guess_number < num:
            print("Too Low")
            attemp -= 1
            keep_guessing = True
        elif guess_number == num:
            print(f"You got it! the answer was {num}")
            return 
        else:
            print("It is not a number")
            keep_guessing = True
        if attemp == 0:
            print("You lost your attemps, now is {attemp}!")
            return
        print(f"you have {attemp} attemps to guess the number")
Guessing()