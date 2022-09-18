print("\t\tWelcome to Tip Calculator\n\n")
bill=float(input("What was the total bill? : $"))
percent=int(input("What percentage tip would you like to give? 10,12 or 15? : "))
people=int(input("How many people to split the bill? "))

new_bill=bill+(bill*percent)/100
print(f"Each person should pay : ${round(new_bill/people,2)}")
