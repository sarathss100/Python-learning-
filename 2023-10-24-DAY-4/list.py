names_string = input("Please enter names \n")
names = names_string.split(", ")

import random

names_length = len(names)
random_choice = random.randint(0, names_length - 1)

person = names[random_choice]

print(f"Seleced person to pay the bill is {person}!")