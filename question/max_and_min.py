list_numbers = [12,45,0,35,24,7]

max = list_numbers[0]
min = list_numbers[0]

for i in list_numbers:
    if (max < i):
        max = i
    if (min > i):
        min = i

print("Max value: ", max, " Min value: ", min)