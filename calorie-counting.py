def calorie_counting(calories):
    return sum(map(int, calories.split("\n")))

with open("input.txt") as file:
    map_object = map(calorie_counting, file.read().split("\n\n"))
    list_object = list(map_object)
    list_object.sort()
    l = len(list_object)
    
print("the most calories :")
print(list_object[-1])
print("the sum of the three most calories :")
print(sum(list_object[l-3:l]))