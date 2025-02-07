# funnction is a blobk of code which only runs when it is called

# def -> keyword function in python

x = 30
y = 40

def my_function(x,y):
    z = x + y
    return z

result = my_function(x,y)

def my_first_function():
    print("Hello World")

print(result)
my_first_function()


def  my_function_name(*kids):
    print("The youngest chilg is " + kids[2])

my_function_name("Carlos", "Emilia", "Roberto")


def food_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

food_function(fruits)