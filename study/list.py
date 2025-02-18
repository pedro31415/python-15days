thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist)
print(thislist[2])

for fruits in thislist:
    print(fruits)

# length the variable
print(len(thislist))

# type data
print(type(thislist))
print(thislist[-2])

print(thislist[1:5])

thislist[1] = "strawberry"

print(thislist)

thislist.pop()
print(thislist)

thislist.insert(5, "mango")
print(thislist)

thislist.append("blacberry")
print(thislist)

thislist.remove("orange")
print(thislist)

for i in range(len(thislist)):
    print(i)

numberslucky = [2,3,34,5,12,1,10]

result  = numberslucky.sort()
print(result)

exampleJoin = thislist + numberslucky
print(exampleJoin)