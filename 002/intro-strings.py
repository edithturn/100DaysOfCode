# Data Tyypes adn How Manipulate Strings

# Strings
# Priting the second element in an array of the word "Hello"
print("Hello"[1])
street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# If I add an string to another string these will be contantenated
print("123" + "345")

# Integer
## Adding two numbers it will add the number to the first one , it instead concatenated strings.
print(123 + 451)

# Float
print(123.145)
mystery = 734_529.678
print(type(mystery))

# Boolean
print(True)
print(False)

# Type Error, Type Checking and Type Conversion
# This code gives erro bcz we can't concatenate integers with strings
num_char = len(input("What is your name?"))
print(type(num_char))
#print("You name has" + num_char + "characteres.")


# Let's fix the previos error, now we are converting the int varaible into string to be able to concatenate with other strings
num_char = len(input("Insert your name?"))
new_num_char = str(num_char)
#print("Your name has " + new_num_char + " characters.")


# Data Types
a = 123
b = str(123)
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>


# Mathematical Operations
print (3 * 3 + 3 / 3 - 3)  # 7.0
print (3 * (3 + 3) / 3 - 3) # 3.0

# Number manipulation and F String
print( 8 / 3) # This print a number in float with all the decimal numbers
print(round(8 / 3)) # Round the number just a digit
print(round(8 / 3, 2)) # round the number with two decimal places

# If we want just a integer
print(8 // 3) # Round the number to a one digit "2"

# Incremental operation
result = 4 / 2
result /= 2
print(result) # It is printing 1.0

# Convert all what I want to print in String

score = 0
my_height = 1.5
isWinnning = True
#f-String
print(f"your score is {score}, and you height is {my_height}")