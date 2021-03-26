import os
import art
from game_data import data
import random


def formatAccount(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}, {account['follower_count']}"

def game():
    print(art.logo)
    score = 0
    gameContinue = True
    # Initializing
    optionA = random.choice(data)
    optionB = random.choice(data)
    

    while gameContinue:
        optionA = optionB
        optionB = random.choice(data)

        while optionA == optionB:
            optionB =  random.choice(data)
        
        # Printing options
        print(f"Compare A : {formatAccount(optionA)}")
        print(art.vs)
        print(f"Against B : {formatAccount(optionB)}")
        choose = input("Who has more followers Type 'A' or 'B' : ")
        print(f"Choose {choose}")
         
        #is_correct = checkAnswer(choose, optionA['follower_count'], optionB['follower_count'])

        if optionA['follower_count'] > optionB['follower_count']:
            if choose.lower() == "a":
                is_correct = True
            else:
                is_correct = False
        else:
            if choose.lower() == "b":
                is_correct = True
            else:
                is_correct = False

        #os.system('clear')
        print(art.logo)
        if is_correct:
            score += 1
            print(f"You are right! Current score{score}")
        else:
            gameContinue = False
            print(f"Sorry, tha's wrong Final score {score}")

game()

