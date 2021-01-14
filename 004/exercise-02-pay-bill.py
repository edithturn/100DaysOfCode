import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

index_name =  random.randint(0, len(names) -1)
print(len(names))
name = names[index_name]
print(f"{name} is going to buy the meal today!")