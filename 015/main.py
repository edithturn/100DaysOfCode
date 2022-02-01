MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def ask_user_preferences(choose):
    drink_cost = MENU[choose]["cost"]
    if choose in MENU: 
        user_credit = process_user_credit()
        if user_credit < drink_cost:
            print(f"Sorry that's not enough money. Money refunded.")
        else:
            if user_credit > drink_cost:
                diference = calculate_change(user_credit, drink_cost)
                print(f"Here is ${diference} in change")
            print(f"Here is your {choose} ☕. Ejoy!")
            update_resources(choose, drink_cost)

def validate_transaction():
    if resources['water'] <= 0:
        print("Sorry there is not enough water.")
        return False
    if resources['milk'] <= 0:
        print("Sorry there is not enough milk.")
        return False
    if resources['coffee'] <= 0:
        print("Sorry there is not enough coffee.")
        return False
    return True

def check_resources_sufficient():
    #ingredients = MENU[choose]["ingredients"]
    print(f"water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"profit: {profit}")

def calculate_change(user_credit, cofe_cost):
    return round(user_credit - cofe_cost, 2)

def update_resources(choose, drink_cost):
    resources['water']  -= MENU[choose]["ingredients"]["water"]
    resources['milk']  -= MENU[choose]["ingredients"]["milk"]
    resources['coffee']  -= MENU[choose]["ingredients"]["coffee"]
    global profit
    profit += drink_cost

def process_user_credit():
    #Quarters 0.25  Dimes 0.10  Nickles 0.05 Pennies 0.01
    print(f"Please insert coins: ")
    quarters = input("How many quarters? ")
    dimes = input("How many dimes? ")
    nickles = input("How many nickles? ")
    pennies = input("How many pennies? ")

    user_credit = float(quarters) * 0.25 + float(dimes) * 0.10 + float(nickles) * 0.05 + float(pennies) * 0.01
    return user_credit

is_on = True

while is_on:
    if validate_transaction() == False:
       break
    else:
        choose = input("What would you like? (espresso/latte/cappuccino) : ")
    
    if choose == "off":
        is_on = False
    elif choose == "report":
        check_resources_sufficient()
    else:
        ask_user_preferences(choose)