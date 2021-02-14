order = {
    "starter": {1:"Sald",2 :"Soup"},
    "main":{1:["Burguer","Fries"],2:["Steak"]},
    "dessert":{1:["Ice Cream"], 2:[]}
}

print(order["main"][2][0])


starting_dictionary = {
    "a" : 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b":8,
    "c":7,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary) 