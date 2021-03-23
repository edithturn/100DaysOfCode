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
def thinkRandomNumber():
    num = random.randint(1, 100)
    return num

keep_asking = True

while keep_asking:
    difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard' : ")
    if difficulty.lower() == "easy":
        attemps = 5
        keep_asking = False
    elif difficulty.lower() == "hard":
        attemps = 10
        keep_asking = False



print(thinkRandomNumber())