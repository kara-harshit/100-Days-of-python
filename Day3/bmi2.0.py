height=float(input("Enter your height in m : "))
weight=float(input("Enter your weight in kg : "))

bmi=round(weight/height**2)
if bmi<18.5:
    print(f"your BMI is {bmi}, you are under weight")
elif bmi>18.5 and bmi<25:
    print(f"your BMI is {bmi}, you have nomral weight")
elif bmi>25 and bmi<30:
    print(f"your BMI is {bmi}, you are overweight")
elif bmi>30 and bmi<35:
    print(f"your BMI is {bmi}, you are obese")
elif bmi>35:
    print(f"your BMI is {bmi}, you are clinically obese")