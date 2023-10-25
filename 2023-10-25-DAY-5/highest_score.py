scores = input("Please enter the scores : \n").split()

num = 0

for n in scores:
    score = int(n)
    scores[num] = score
    num += 1

heighest_score = 0

for x in scores:
    if heighest_score < x:
        heighest_score = x

print(f"Heighest score is : {heighest_score}")