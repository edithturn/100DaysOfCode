import os
import art
import game_data
import random

def changingOptions():
    print(art.logo)
    # Calculing optionA
    optionA = game_data.data[random.randint(1, len(game_data.data) - 1)]
    final_list = []
    print(f"Compare A: {optionA['name']}, {optionA['description']}, from {optionA['country']} {optionA['follower_count']} .")
    print(art.vs)

    # Calculing optionB
    optionB = game_data.data[random.randint(1, len(game_data.data) - 1)]
    print(f"Against B: {optionB['name']}, {optionB['description']}, from {optionB['country']} {optionB['follower_count']}.")

    # Which option has more followers
    if optionA['follower_count'] > optionB['follower_count']:
        num_to_compare = optionA['follower_count']
    else:
        num_to_compare = optionB['follower_count']
    # Saving the name that already was choose in the list to avoid show again
    final_list.append(optionA['name'])
    final_list.append(optionB['name'])
    print(final_list)

    # Comparing the answer of the user with the max follower option
    # Changing the optionA and optionB depending of the selection of the user
    choose = input("Who has more followers Type 'A' or 'B' : ")
    if choose.lower() == 'a':
        user_choose = optionA['follower_count']
        if user_choose  == num_to_compare:
            optionA = optionA
    elif choose.lower() == 'b':
        user_choose = optionB['follower_count']
        if user_choose == num_to_compare:
            optionA = optionB
    else:
        print("You shoul type A or B")

    while optionB['name'] in final_list:
        _random = random.randint(1, len(game_data.data) - 1)
        optionB = game_data.data[_random]
    os.system('clear')
    print(f"Compare A: {optionA['name']}, {optionA['description']}, from {optionA['country']} {optionA['follower_count']} .")
    print(art.vs)
    print(f"Against B: {optionB['name']}, {optionB['description']}, from {optionB['country']} {optionB['follower_count']}.")

def compareItems():
    # Initializing
    optionA = {}
    optionB = {}
    final_list = []
    score = 0
   
    # Take the input from the use
    choose = ""
    keepAsking = True
    while keepAsking:
        choose = input("Who has more followers Type 'A' or 'B'")
        if choose.lower() == 'a':
            user_choose = optionA['follower_count']
            keepAsking =  False
            if num_to_compare == user_choose:
                core += 1
        elif choose.lower() == 'b':
            user_choose = optionB['follower_count']
            keepAsking = False
            if num_to_compare == user_choose:
                core += 1
                optionA = optionB
                showOptions()
        else:
            print("You shoul type A or B")
    
    
    _len = len(final_list)
    while _len < len(game_data):
        if score <= 0:
            print("You lost the game:")
            return
            if game_data['name'] != final_list['name']:
                final_list.append(optionA)
                final_list.append(optionA)
        elif score > 0:
            continue
            print("You won!")

        _len += 1
        

        
    print(optionA)
    print(optionB)



changingOptions()
