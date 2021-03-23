
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



game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 4:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()

# Modifying Global Scope

soldiers = "Skeleton"

def increaseEnemies():
    soldiers = "Zombie"
    print(f"soldiers inside function: {soldiers}")

increaseEnemies()
print(f"soldiers inside function: {soldiers}")



# Modifying Global Scope

soldier = 1

def increaseSoldiers():
    global soldier
    soldier += 2
    print(f"Soldier inside function: {soldier}")

increaseSoldiers()
print(f"Soldier inside function: {soldier}")
