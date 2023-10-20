print("Welcome to Leap Year Calculator")

year = int(input("Please enter a year to check : "))

if year % 4 == 0 and year % 100 != 0:
    print("Entered year is a Leap Year!")
elif year % 4 ==0 and year % 100 == 0 and year % 400 == 0:
    print("Entered year is a Leap Year!")
else:
    print("Entered year is not a Leap Year!")