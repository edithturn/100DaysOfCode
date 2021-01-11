height = int(input("enter your height in cm: "))
age = int(input("Type your age:"))
photos = input("Type Yes or Not:")
ticket_price = 50


if height > 120:
    print("Can ride!")    
    if age < 12:
        ticket_price += 5
    elif age > 12 and age < 18:
        ticket_price += 7
    else:
        ticket_price += 12
    if photos == "Yes":
        ticket_price += 3
    print(f"The total price is ${ticket_price}")
else:
    print("You can't drive!")

