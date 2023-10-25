#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

simple_password = []

num1 = 1

for letter in letters:
    if num1 <= nr_letters:
        simple_password.append(random.choice(letters))
        num1 += 1
    else:
        break

num2 = 1

for symbol in symbols:
    if num2 <= nr_symbols:
        simple_password.append(random.choice(symbols))
        num2 += 1
    else:
        break

num3 = 1

for number in numbers:
    if num3 <= nr_numbers:
        simple_password.append(random.choice(numbers))
        num3 += 1
    else:
        break

random.shuffle(simple_password)

complex_password = ""

for n in simple_password:
    complex_password += n

print(f"Your password is : {complex_password}")