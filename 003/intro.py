# Contional Statement, Logical Operators, Code Blocks and Scope

# Example of a conditional Operators

if condition:
    do this
else:
    do this

# Example
water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

# Indentations | elif
hight = input("What is your hight in cm?")

if hight > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please, pay $5.")
    elif age <= 18:
        print("Please, pay $7.")
    else:
        print("Please, pay 12$.")
else:
    print("Sorry, you have to grow taller before you can ride.")
