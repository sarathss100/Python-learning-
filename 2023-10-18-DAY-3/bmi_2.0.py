print("Welcome to BMI Calculator")

weight = int(input("Please enter your weight Kg : "))
height = float(input("Please enter your height in cm : "))

bmi = weight / (height / 100) ** 2

if bmi < 18.5:
    print(f"Your BMI is {round(bmi, 2)} and you are Under weight")
elif bmi <= 25:
    print(f"Your BMI is {round(bmi, 2)} and you are Normal")
elif bmi <= 30:
    print(f"Your BMI is {round(bmi, 2)} and you are Slightly Over Weight")
elif bmi <= 35:
    print(f"Your BMI is {round(bmi, 2)} and you are Obese")
else:
    print(f"Your BMI is {round(bmi, 2)} and you are Clinicaly Obese")