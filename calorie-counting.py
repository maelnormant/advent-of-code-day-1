most_calories = 0
calories = 0
tables = []

with open("input.txt") as file:
    for line in file:
        tables.append(line)
for i, calorie in enumerate(tables):
    if calorie != "\n" and calorie != "end\n":
        calories += int(calorie)
    if tables[i+1] == "\n":
        if calories > most_calories:
            most_calories = calories
        calories = 0
    if tables[i+1] == "end\n":break
print(most_calories)
