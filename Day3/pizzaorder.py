print("Welcome to pizza Deliveries!")
size=input("What size pizza do you want? S,M or L : ")
add_pepperoni=input("Do you want pepperoni? Y or N : ")
extra_cheese=input("Do you want extra cheese? Y or N : ")
total_bill=0
if size=='S' or size=='s':
    total_bill=15
elif size=='M' or size=='m':
    total_bill=20
elif size=='L' or size=='l' :
    total_bill=25

if add_pepperoni=='Y' or add_pepperoni=='y':
    if size=='s':
        total_bill=total_bill+2
    else:
        total_bill+=3

if extra_cheese=='Y' or extra_cheese=='y':
    total_bill+=1

print(f"your total bill is ${total_bill}")
input("\n\n\n\nPress enter to exit: ")
