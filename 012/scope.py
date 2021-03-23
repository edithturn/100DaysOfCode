
################ scope ###############################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

#drink_potion()
# This line will give us an error because the variable doesn't exist
#print(potion_strength) 
    
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(f"Inside the function: {player_health}")


    drink_potion()
print(f"Outside the function: {player_health}")