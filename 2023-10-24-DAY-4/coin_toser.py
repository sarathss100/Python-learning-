import random

print("Welcome to coin toser!")

side = random.randint(0,1)

if side == 0:
    print("Heads")
else:
    print("Tails")