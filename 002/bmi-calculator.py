#  Body Mass Index

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

int_height = float(height)
int_weight = float(weight)

bmi = int_weight/(int_height ** 2)
print(int(bmi))