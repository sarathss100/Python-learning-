print("Welcome to BMI Calculator")

weight = int(input("Please enter your weight in Kg  :\n"))
height = int(input("Please enter your height in cm : \n"))

height_meter = height/100

BMI = weight / height_meter**2

print("Your BMI is " + str(round(BMI,2)))