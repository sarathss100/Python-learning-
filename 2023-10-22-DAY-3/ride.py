print("Welcome to Derby Ride")

height = int(input("Please enter your height? \n"))
age = int(input("Please enter your age? \n"))
bill = 0

if height >= 120:
    if age < 10:
        bill = 5
        print(f"Your payment for the ride is ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Your payment for the ride is ${bill}")
    else:
        bill = 10
        print(f"Your payment for the ride is ${bill}")

    photo = input("Do you need a photo, Yes or No? \n")
    if photo == "Yes":
        bill += 3
    print(f"Your total payment for the ride is ${bill}")

else:
    print("Sorry you are not eligible for this ride!")