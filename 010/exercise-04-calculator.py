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

operation_symbol = input("Pick an operation from the line above:")
num2 = int(input("What is the second number?"))

calculation_function = operations[operation_symbol]
answer = calculation_function(num2, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")