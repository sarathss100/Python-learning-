print("Welcome to Peppe Pizza")

pizza_size = input("Please choose the size of pizza, \n'L' for large pizza $25 \n'M' for medium $15 \n'S' for small $10 \n")

bill = 0

if pizza_size == "S":
    bill += 10
    pizza_pepporoni = input("Add pepparoni in in small pizza? Y or N \n")
    if pizza_pepporoni == "Y":
        bill += 2
    pizza_cheese = input("Add extra cheese in in small pizza? Y or N \n")
    if pizza_cheese == "Y":
        bill += 1
        print(f"Your grand total bill is ${bill}")
    else:
        print(f"Your grand total bill is ${bill}")
elif pizza_size == "M":
    bill +=15
    pizza_pepporoni = input("Add pepparoni in in Medium pizza? Y or N \n")
    if pizza_pepporoni == "Y":
        bill += 3
    pizza_cheese = input("Add extra cheese in in Medium pizza? Y or N \n")
    if pizza_cheese == "Y":
        bill += 1
        print(f"Your grand total bill is ${bill}")
    else:
        print(f"Your grand total bill is ${bill}")
else: 
    bill +=25
    pizza_pepporoni = input("Add pepparoni in in Large pizza? Y or N \n")
    if pizza_pepporoni == "Y":
        bill += 3
    pizza_cheese = input("Add extra cheese in in Large pizza? Y or N \n")
    if pizza_cheese == "Y":
        bill += 1
        print(f"Your grand total bill is ${bill}")
    else:
        print(f"Your grand total bill is ${bill}")

