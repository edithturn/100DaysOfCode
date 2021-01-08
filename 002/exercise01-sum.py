# Asking a string data, a number with a digit
two_digits = input("Type a two digit number: ")

# Taking the first digit and the second digit of the number to convert in int before to do the addition
sum = int(two_digits[0]) + int(two_digits[1])

# Printing the addition of the numbers, before print It is converting in string, to be able to concatenate with a string
print ("Your addition is: " + str(sum))