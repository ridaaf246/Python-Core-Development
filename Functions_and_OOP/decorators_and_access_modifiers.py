# A decorator is a function that adds extra functionality to another function 
# without modifying its original code. 
# It takes a function as an argument, 
# wraps it with additional code, 
# and returns a new function.

# def decorator_name(function):
#     def wrapper():
#         # Code before the original function
#         function()
#         # Code after the original function
#     return wrapper

# @decorator_name
# def function_name():
#     statements

# function_name()

def hi(f):
    def greet():
        print("hi")
        f()
    return greet

@hi
def sir ():
    print("hehehe")

sir()



def greet (a):
    def hello ():
        print("hello sir how are you")
        a()
    return hello 

@greet
def service():
    print("what you want")

service()


# Create a decorator that prints "Before execution" before the function and "After execution" after the function. Decorate a function named message() that prints "Hello Python".

def deco(a):
    def printing():
        print("Before execution") # statements here execute before executing decorater
        a()
        print("After Execution")  # statements here execute after executing decorater

    return printing
@deco
def message():
    print("Hello Python")

message()


# Create a decorator that prints "Calculating result..." before a function. Decorate a function named add() that takes two numbers and prints their sum.

def deco(a):
    def sum(c,b):
        a()
        print (c + b)
    return sum

@deco
def result():
    print("Calculating result...")

result(2, 4)




class employee:
    def __init__(self):
        self.__name = "Zain" # become private attribute, can't access outside of class due to __
        self.name = "Rida"
a = employee()
# print(a.__name) # can't accessed outside of class because it become private because of __
# to access it
print(a._employee__name) # use this method
print(a.name)

a = print(a.__dir__()) # print all functions
print(type(a))