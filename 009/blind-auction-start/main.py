import art
import os
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

option = False
auction_dic = {}

def fill_dic(name, amount):
    auction_dic[name] = amount

while not option:
    name = input("Name:")
    amount = int(input("What is your bid?"))
    fill_dic(name, amount)
    selecction = input("Do yo have more? yes or no \n")
    if selecction == "no":
        option = True
    os.system('clear')

auction_max = max(auction_dic.values())
print(auction_dic)
print(auction_max)