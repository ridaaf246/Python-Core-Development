### GLOBAL AND LOCAL VARIABLE ###
a = 6 # global variable is defined outside the function

def printing():
    x = int(input("Enter number: ")) # local variable is defined in function, can be accessed only in function
    y = "You write number less than 5"
    if x >= 5 :
      print("Hello")
    else:
       print(y)
       print(a) # local varibale can be accessed in the fucntion

printing()
print(a)
# print(x) # global variable can't be accessed outside the function
# print(y) it is error because y is defined in function, and we call it outside the function



# If you want to change the value of a global variable inside a function,
# you must use the `global` keyword.
# Write `global variable_name` at the beginning of the function (before changing its value).
# After that, you can change the variable just like a normal variable (a = 8).

a = 5  # Global variable

def printing():
    global a  # Must be declared before modifying the global variable
    x = 10
    a = 8      # Changes the global variable
    y = 0
    print(y)
    print(x)

printing()
# Since the global variable was changed inside the function,
# it now has the updated value (8) instead of its original value (5).
print(a)



### LAMBDA ###
def double(x):
   return x*2

print(double(45))


double = lambda x: x*2 # above function can be written like this
print(double(45))

sum = lambda x: x + x / 2
print(sum(7))

avg = lambda x, y, z: x + y + z / 3
print(avg(7, 9, 4))



### MAP ###
def cube(x):
   return (x*x*x)

print(cube(6))

l = [1, 3, 2, 7, 5, 4]
new = list(map (cube,l))  # map keyword is used to perform specific fucntion on a list, tuple
print(new)

 

### FILTER ###


def filter1(a):
   return a >4 
l = [1, 3, 2, 7, 5, 4]

new = list(filter(filter1,l))  # give us selective data according to our choice
print(new)


def filter1(a):
   return a == "hello"

l = ["hell", "hello", "hi", "hello"]
new = list(filter(filter1,l))
print(new)



### REDUCE ###

from functools import reduce

def sum(x, y):
   return x+y

l = [1, 3, 2, 7, 5, 4]
new = reduce(sum,l)
print(new)



l = ["hell", "hello", "hi", "hello"]
new = reduce(sum,l)
print(new)



from functools import reduce

def avg(x, y):
   return x+y/2

l = [1, 3, 2, 7, 5, 4]
new = reduce(avg,l)
print(new)



###  is AND == ###
# both are comparison operators
# is compare exact location of object in memory
# == compare exacct values
# print ture or false according to conditions

a = 4
b = "4"
print(a is b)  
print(a == b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) 
print(a == b)

a = 2
b = 2
print(a is b) 
print(a == b)


a = (1, 2, 3)
b = (1, 2, 3)
print(a is b) 
print(a == b)


a = "hello" # can be performed also on strings
print(a is "hello")
print(a == "hello")



x = [1, 2, 3]
print (dir(x)) # tell which method we can apply on specific data
print(x.clear)

x = 1, 2, 3
print (dir(x))
a = (x.__reduce__)
print(a)

x = (1, 2, 3)
print (dir(x))
a = x.__add__((4, 5, 6))
print(a)

