import csv

tables = []
calories = 0
sums = []

with open('input.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for line in reader:
        tables.append(line)
for i, calorie in enumerate(tables):
    if len(calorie) == 1:
        calories += int(calorie[0])
    if calorie != tables[-1]:
        if len(tables[i+1]) == 0:
            sums.append(calories)
            calories = 0
sums.sort()
sums.reverse()
print("the most calories :")
print(sums[0])
print("the sum of the three most calories :")
print(sum(sums[0:3]))
