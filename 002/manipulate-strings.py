# Data Tyypes

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


