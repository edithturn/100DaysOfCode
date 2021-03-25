import art
import game_data
import random

print(art.logo)

def showOptions():
    
    optionA = game_data.data[0]
    _ran = random.randint(1, len(game_data.data) - 1)
    optionB = game_data.data[_ran]
    print(f"Compare A: {optionA['name']}, {optionA['description']}, from {optionA['country']}.")
    print(f"Against B: {optionB['name']}, {optionB['description']}, from {optionB['country']}.")


showOptions()