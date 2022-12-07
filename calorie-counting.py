calories = 0
tables = []
sums = []

with open("input.txt") as file:
    for line in file:
        tables.append(line)
for i, calorie in enumerate(tables):
    if calorie != "\n":
        calories += int(calorie)
    if calorie != tables[-1]:
        if tables[i+1] == "\n":
            sums.append(calories)
            calories = 0
sums.sort()
print("the most calories :")
print(sums[-1])
print("the sum of the three most calories :")
print(sums[-1]+sums[-2]+sums[-3])
