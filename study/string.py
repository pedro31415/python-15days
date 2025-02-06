# "hello" and 'hello' is same example of string

print("Hello")
print('Hello')

a = "Hello"

print(a)

a = "hello, world!"

print(a[2])

# for x in a:
#     print(a)

# looping through a string
for x in "banana":
    print(x)

# String Length

name = "Pedro Henrique Araujo Cardoso"
clean_name = name.strip()

print("Space: ", len(name), " No space: ", len(clean_name))
# string present in the all text
print("Pedro" in name)


# slice of string
last_name = name[5:]
print(name[0:5])
print(last_name)

# modify string

best_name = name.upper()
print(best_name)

worst_name = name.lower()
print(worst_name)

a = "PPPPPE"
print(a.replace("P", "K"))

# method split
b = "Hello, World"
print(b.split(","))

concatenation = a + b
print(concatenation)

age = 46
txt = f"my name is Pedro and my age is {age}"

print(txt)
print(txt.capitalize())


print(5 > 10)

value_one = 200
value_two = 33

if value_one > value_two:
    print(f"value_one {value_one} is greater than value_two {value_two}")


print(bool("Hello"))
print(bool())