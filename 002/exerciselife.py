age = input("What is your current age? ")

years_left = 90 - int(age)

life_in_days = years_left * 365
life_in_weeks = years_left * 52
life_in_months = years_left * 12

print(f"You have {life_in_days} days, {life_in_weeks} weeks, {life_in_months} months left")