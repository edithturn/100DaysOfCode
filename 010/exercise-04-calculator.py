def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

operations = {
"+": add,
"-": sub,
"*": mult, 
"/": div
}

num1 = int(input("What is the first number? "))

for key in operations:
    print(key)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What is the second number? "))

# Using the parameter operation_symbol to search into the dictionary 
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

keep_calculating = False

while keep_calculating == False:    
    option = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.: ")
    if min(option) == 'y':
        operation_symbol1 = input("Pick another operation: ")
        num3 = int(input("what's the next number? "))
        calculation_function1 = operations[operation_symbol1]
        second_answer = calculation_function1(first_answer, num3)
        print(f"{first_answer} {operation_symbol1} {num3} = {second_answer}")
        first_answer = second_answer
    elif min(option) == 'n':
        keep_calculating == True
        break
    else:
        print("You didn't type any value!")