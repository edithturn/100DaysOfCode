# import random

# random_number = random.randint(0, 1)
# print("Heads") if random_number == 1 else print("Tails")

states_of_america = ["California", "Georgia", "Virginia"]

# First element in the list
print(states_of_america[0])

# Last element in the list
print(states_of_america[-1])

states_of_america[0] = "Cali"
print(states_of_america)

states_of_america.append("Fenix")
print(states_of_america)

states_of_america.extend(["Jack Bauer", "NY"])
print(states_of_america)