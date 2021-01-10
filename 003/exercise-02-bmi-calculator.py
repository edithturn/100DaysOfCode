"""Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

BMI = weight(kg)/height^2 (m^2)"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight/(height**2)
interpretation = ""
if bmi < 18.5 :
    interpretation = "You are underweight"
elif bmi > 18.5 and bmi < 25:
    interpretation = "You have a normal weight"
elif bmi > 25 and bmi < 30:
    interpretation = "You are slightly overweight"
elif bmi > 30 and bmi < 35:
    interpretation = "You are obese"
else:
    interpretation = "You are clinically obese"

final_bmi = "{:.0f}".format(bmi)
print(f"Your BMI is {final_bmi}, {interpretation}")