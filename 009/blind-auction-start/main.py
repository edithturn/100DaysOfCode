import art
import os
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

option = False
auction_dic = {}

def fill_dic(name, amount):
    auction_dic[name] = amount

def finding_max(auction_dic):
    highest_bid = 0
    winner = ""
    for n in auction_dic:
        bid_amount = auction_dic[n]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = n
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not option:
    name = input("Name:")
    amount = int(input("What is your bid? \n"))
    fill_dic(name, amount)
    selecction = input("Do yo have more? [yes] or [no] \n")
    if selecction == "no":
        option = True
    os.system('clear')

finding_max(auction_dic)
print(auction_dic)
