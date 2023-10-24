line_1 = [0, 0, 0]
line_2 = [0, 0, 0]
line_3 = [0, 0, 0]

map = [line_1, line_2, line_3]
print("Hiding your treasure, x marks the spot")
position = input("Where do you want to put the treasure ? \n")

x = position[0].lower()
# This is my solution
#if x == "A":
#    x = 0
#elif x == "B":
#    x = 1
#else:
#    x = 2
abc = ["a", "b", "c"]
value_1 = abc.index(x)
value_2 = int(position[1])

map[value_1][value_2] = "x"

print(f"{line_1}\n {line_2}\n {line_3}")
