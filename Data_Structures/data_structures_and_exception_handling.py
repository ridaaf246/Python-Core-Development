### LIST AND TUPLE ###

a = [2, 5, 35, 4, 55, 90, 43, "student", 0]

if 7 in a:   # use to find something in our data
    print("FOUND")
else:
    print("NOT FOUND")


if "pr" in "pray":  
    print("TRUE")

print(a)

### list comprehension ###

lst = [i for i in range(10)] # list can be printed using for loop
print(lst)

lst = [i*i  for i in range(10)]
print(lst)

lst = [i*i  for i in range(10) if i %2 ==0] # can put a condition like this
print(lst) 


# how to count something in your list
a = [2, 8, 35, 4, 55, 90, 43, "student", 0]
print(a.count(4))
print(a.count(6))
print(a.count(5))

print(a)
b = a
b[0] = 0
print(a)

l = [34, 44, 66,34,32,32]
print(l)
m = [99, 67,88]
l.extend(m)  # add something new at the end of the list
print(l)
     
     # or

l = [34, 44, 66,34,32,32]
print(l)
m = [99, 67,88]
print(m)
k = m+l
print (k)


a = [2, 4, 6, 8, 10]
print(a)

a [0] = 0, 2 # can add something on specific index in list
print (a)

a = [2, 4, 6, 8, 10]
a [4] = 0
print (a)


tup = (0, 1, 2, 3, 4, 5, 6, 7)

tup1 = tup[3 : 5]  # process of slicing, can be done in list, tuple both, write index from where you want to start : write index where you want to end
print(tup1)

if 233 in tup:
    print("YES")
else:
    print("NO")
 
b = tup.count(1) # know how many time a specific element exist in data
print(b)


tup = (10, 1, 2, 2, 0, 3, 4, 0, 5, 6, 7, 8, 9, 0)

b = tup.index(4)  # get index of specifc element, in bracaket we write element to find
print(b)
b = tup.index(2, 0, 7) # first we write which element to find, then from which index to which index
# Search for 2 starting at index 0 and ending before index 7.
print(b)

# tup.index(4) finds 4 at index 6.
# tup.index(2, 0, 7) searches between indices 0 and 6 (7 is not included) and returns the first occurrence of 2, which is at index 2.




### STRING FORMATING ###

a = "Hi! My name is {} and i am from {}"
name = "Rida"
country = "Pakistan"

print(a.format(name,country)) # old method to adjust your data in string


a = "Hi! My name is {1} and i am from {0}" # where 0 is, there that variable will print that is at index 0 in our statement
name = "Rida"
country = "Pakistan"

print(a.format(country, name)) # same can be done like this also, but need to put indexes in the variable braces
     
        #or
    

name = "Rida"
country = "Pakistan"
print(f"Hi! My name is {name} and i am from {country}") # in this method, we write directly our variable name in the braces # f is part to syntax for formatting
print(f"Hi! My name is {{name}}and i am from {{country}}")  # showig curly braces to show braces on screen , it will not print variable data, show as it is
print("Hi! My name is", name, "and i am from ", country) # can be done like this as well, that's easy bro 👀💁‍♀️, also don't have braces issue if accidently forget f

price = 49.09999
txt = f"for only {price :.2f} dollars" # this way can decide decimals after point
print(txt)

txt = f"for only {price :.8f}"
print(txt)



  ### DOCSTRING ###

def square (n):
    """taking square of n""" # this is a docstring, not a comment. This doesnot print until we don't use operation to print it
    '''taking square of n'''  #can be writeen like this also, docstrings use write just below the functiond definition and use to documnet our code
    # docstring is written just below the function definition, just like in this code, the first like is only considered as a docstring and it will only be printed when we use docstring operation
    print(n**2)

square(5)
print(square.__doc__)  # operation to use doc string, this will print doc string


def square (n):
    print(n)
    """taking square of n""" # this will not be a docstring, because docstring is available just below the the fucntion definition
square(5)
print(square.__doc__)





### PEP 8 ###
# python enhancement porposal
# provide guideline and best practice for python code
# these are documents


### ZEN PF PYTHON ###
# type ""import this"" in your terminal
# you will get a poem that is beneficitial




def fact (n):
    if (n == 0 ):
        return 1
    else:
        return n * fact (n-1)

print(fact(3))



def fact (n):
    if n == 0:
        return 
    else:
        print(n*n)

fact (2)
fact (0)




def series (n):
    print((n-1)+(n-2))

series(5)



set = {2, 5, 3, 5}
print(set)
print(type(set))




### DICTIONARY ### 
info = {
    'name' : "Rida",
    'clas' : "BS",
    'roll_no' : "12"
}

print(info)
print(info.keys()) # print all dicntionary keys
print(info.values()) # print all dictionary values
print(info.items()) # print all dictionary items 


# we can use else with for, while loop also 


### ERROR HANDLIG ###

# by using this, we can handle error
# if we use this method, then there will be no error if the user put wrong input
#     try:
#         our statements
#     except:
#          our statements
a = input("Enter number: ")
try:                               
 for i in range(1, 11):
    print(f"{a} x {i} = {int(a)*i}")
except:
    print("You enter wrong data.")

print("The table has been printed")


a = input("Enter number: ")
try:                               
 for i in range(1, 11):
    print(f"{a} x {i} = {int(a)*i}")
except Exception as b:  # default method for error,   "except exception as" is the part of syntax, we can use variable what we want
    print(b)  # this will print statement by python
    

print("The table has been printed")

a = input("Enter number: ")
try:                               
 for i in range(1, 11):
    print(f"{a} x {i} = {int(a)*i}")
except ValueError:
   print("Value Error")



a = input("Enter number: ")
try:                               
 for i in range(1, 11):
    print(f"{a} x {i} = {int(a)*i}")
except: 
    print("You enter wrong data")
finally:    # this will always be excecuted, no matter try excute or except, conditiion does not matter for this, it will always execute
   print("Do you want to try again?")


a = input("Enter number: ")
                        
for i in range(1, 11):
    print(f"{a} x {i} = {int(a)*i}")


a = int (input("enter value between 5 and 9: "))
if (a < 5 or a >9):
   raise ValueError("Value should be between 5 and 9 :()") # if we want to put error in a case that user input wrong data, we will use this method to stop the code


a = int (input("enter value between 5 and 9: "))
if (a < 5 or a >9):
   raise ValueError






 # write a code where value between  5 and 9 or equal to it and quit doesnot show error
a =  (input("enter value between 5 and 9: "))

if ((a == "quit") or (int(a) >= 5) and (int(a)<= 9) ):
    print("You enter correct data")

else:
   raise ValueError





### SHORT HAND IF ELSE STATEMENT ###

a = int(input("Enter your age: "))
print("Adult") if a >= 18 else print("Minor")   # this way we write one lince if else program
print("Adult") if a >= 18 else " "   # we do this if don't want to print something in case of false condition



a = int(input("Enter a number: "))
print("Eligible for discounts") if a >= 5000 else print("No discount")


a = int(input("Enter your age: "))
print("Eligible") if a >= 18 else print("Not eligible")



a = (input("Enter your username: ")).lower()
b = (input("Enter your password: "))
print("Login Successful") if a == "admin" and b == "python123" else print("Invalid user")


### ENUMERATE FUNCTIONS ###

# WITHOUT USING enumerate()
# In this method, the for loop gives only the values from the list.
# We have to create the index variable manually and update it using idx += 1.

idx = 0  
marks = [12, 43, 54, 65, 23, 34, 69]

for mark in marks:
    print(idx, mark)
    if idx == 6:
        print("Highest marks")
    idx += 1  # Manually increasing the index after each loop

# USING enumerate()
# enumerate() automatically provides both the index (position) and value of each item.
# We do not need to create an index variable or update it manually.

marks = [12, 43, 54, 65, 23, 34, 69]

for idx, mark in enumerate(marks):
    print(idx, mark)
    if idx == 6:
        print("Highest marks")



marks = [12, 43, 54, 65, 23, 34, 69]

for idx, mark in enumerate(marks, start = 1):  # this way we change the start value, index will be 1 instaed of 0
    print(idx, mark)
    if idx == 6:
        print("Highest marks")



marks = [12, 43, 54, 65, 23, 34, 69]

for  idx, mark in enumerate(marks):
    print( idx, mark)
    if idx == 6:
        print("Highest marks")


