# Lists of elements
row1 = ["🌴","🌴","🌴"]
row2 = ["🌴","🌴","🌴"]
row3 = ["🌴","🌴","🌴"]

# Join 03 list into a single list
map = [row1, row2, row3]

# Printing the list
print(f"{row1}\n{row2}\n{row3}")
# asking the position of the mark into the map
position = input("Where do you want to put the treasure? ")

# The index of the elements in the lists start in zero, for this example the position is based from 1 to 3, for that reason minus 01 is subtracted
# The input is separated into 02 digits, then converted to integer to substract one
row = int(position[0]) - 1 
col = int(position[1]) - 1

# We can use the indices and put the mark in the place
map[col][row] = "🏺"
print(f"{row1}\n{row2}\n{row3}")

#print(map[2][0])
# 11 00
# 12 01
# 13 02

# 21 10
# 22 11
# 23 12

# 31 20
# 32 21
# 33 22