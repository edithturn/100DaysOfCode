print("welcomer to the tip calculator.")

total_bill = input("What was the tital bill? ")
percentage_bill = input("What percentage tip would you like to give? 10 , 12, or 15?")
qantity_people = input("How many people split the bill? ")


new_percentage_bill = ((int(percentage_bill) / 100) * float(total_bill))  + float(total_bill)
bill_per_person =  new_percentage_bill / int(qantity_people)
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person shou; pay: ${final_amount}")


