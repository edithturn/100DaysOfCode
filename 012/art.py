import random

logo = """
 _  __     _             _     _    _____          _      
 | |/ /    | |           | |   (_)  / ____|        | |     
 | ' / __ _| |_ ___ _   _| |__  _  | |     ___   __| | ___ 
 |  < / _` | __/ __| | | | '_ \| | | |    / _ \ / _` |/ _ |
 | . \ (_| | |_\__ \ |_| | | | | | | |___| (_) | (_| |  __/
 |_|\_\__,_|\__|___/\__,_|_| |_|_|  \_____\___/ \__,_|\___|
                                                 
 """
print("Welcome to the Number Guessing Game!")
print("I am thinking a number betweek 1 and 100")

# variables
num = random.randint(1, 100)

def Game():
    keep_asking_attemps = True
    attemps = 0
    while keep_asking_attemps:
        difficulty = input(f"Choose a difficulty. Type [ easy ] or [ hard ] : ")
        if difficulty.lower() == "easy":
            attemps = 5
            keep_asking_attemps = False
        elif difficulty.lower() == "hard":
            attemps = 10
            keep_asking_attemps = False
    print(f"You have {attemps} attempts remaining to guess the number")
    return attemps

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