thisdict  = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print(type(thisdict))
print(len(thisdict))

# acessing items
print(thisdict["brand"])
print(thisdict.get("brand"))

# get keys

x = thisdict.keys()

print(x)

thisdict["car"] = "Blue"

print(x)

y = thisdict.values()

print(y)

if "model" in thisdict: 
    print("Vale a pena ser feliz")
else: 
    print("Valor não encontrado") 

# thisdict.get("year") = 2018 -> error in system

thisdict["year"] = 2018 # -> correct code

thisdict.update({
    "year": 2020
})

print(thisdict)


# remove elements or keys dictionaries

del thisdict["model"]
print(thisdict)

for x in thisdict:
    print(x)
