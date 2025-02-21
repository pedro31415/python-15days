thisset = {"apple", "banana", "cherry"}

print(thisset)
print(type(thisset))

for x in thisset:
    print(x)

values1 = {1,2,3,4,5,6,7,8,9}
values2 = {2,4,5,6,7,9}

unionvalue = values1.union(values2)
print(unionvalue)

intersction = values1.intersection(values2)
print(intersction)

differencevalue = values1.difference(values2)
print(differencevalue)