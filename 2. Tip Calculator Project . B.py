print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percent = tip/100
pay_amount = (bill + (bill * tip_percent)) / people
print(f"Each person should pay: ${round(pay_amount,2)}")