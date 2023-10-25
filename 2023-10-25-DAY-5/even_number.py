target = int(input("Please enter a limit : "))

sum = 0

for number in range(2, target + 1, 2):
    sum += number

print(f"Sum of even in between limit is : {sum}")