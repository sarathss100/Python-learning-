print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill?\n"))

tip_percentage = int(input("What percentage tip would you like to give?\n"))

people = int(input("How many people to split bill? \n"))

payment = ((total_bill * tip_percentage / 100) + total_bill) / people

split = round(payment, 2)

print(f"Each person should pay: ${split}")