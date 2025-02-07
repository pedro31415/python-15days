i = 1

# while loopings
while (i < 6):
    # print("I am your father!")
    # i += 1
    print(i)
    if i == 3:
        break
    i += 1

# for loopings
fruits = ["Apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]

for x in adj:
    for j in fruits:
        if x == "red" and j == "banana":
            continue
        print(x,j)