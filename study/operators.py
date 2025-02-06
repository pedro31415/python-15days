# Arithmetic operators
x = 10 + 5
print(x)
x  =  10 - 5
print(x)
p = 10 * 5
print(p)
p = 10 / 5
print(p)
p = 11 % 5 
print(p)
p = 10**2
print(p)
# Assignment operators
x += 10
print(x)
# Comparison operators
print(x == p)
print(x != p)
# Logical operators
if(x>10 and x < 20):
    print(x)
if(x>10 or x < 12):
    print(x)
if(not(x>10 and x<20)):
    print(x)
else:
    print("Values is not")
# Identity operators
x  = ["apple", "banana"]
y  = ["apple", "banana"]
z =  x

print(x is z)

print(x is y)

print(x == y)
# Membership operators

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

# Bitwise operators

# & -> AND
# | -> OR
# ^ -> XOR
# ~ -> NOT
# << -> Zero fill left shift
# >> -> Signed right shift
