print("The Love calculator is calculating your score...")

name_1 = input("What is your name? ")
name_2 = input("What is there name? ")

combined_name = name_1 + name_2
upper_name = combined_name.upper()

T = upper_name.count("T")
R = upper_name.count("R")
U = upper_name.count("U")
E = upper_name.count("E")

count_1 = T + R + U + E

L = upper_name.count("L")
O = upper_name.count("O")
V = upper_name.count("V")
E = upper_name.count("E")

count_2 = T + R + U + E

love_score = str(count_1) + str(count_2)

value = int(love_score)

if value < 10 or value > 90:
    print(f"Your score is {value}, you guys go like coke and mentos!")
elif value > 40 and value < 50:
    print(f"Your score is {value}, you guys alright together!")
else:
    print(f"Your score is {value}")