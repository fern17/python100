print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
total_bill = total * (1.0 + (tip_percentage / 100.0))
bill_per_person = total_bill / people
final_amount_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: $ {final_amount_per_person}")
