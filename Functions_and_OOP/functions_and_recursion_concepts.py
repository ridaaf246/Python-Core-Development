### FUNCTION ###

# def function_name(parameters):           
#      Code to execute
#     return value    # Optional

# syntax for fucntion call
#    function_name(arguments)



def sum (a,b):
    print(a + b)

sum (12,32)



def subtract (a,b):
    print(a - b)

subtract (12,32)

def product (a,b):
    print(a * b)

product (12,32)


def division (a,b):
    print(a / b)

division (12,32)


def ave (a , b, c):
    print(a+b+c/3)

ave (12, 32,54)



def average_of_total (a, b, c , d, e, f, g, h):
    print((a+b+c+d+e+f+g+h/8)*100)


a = int(input("Enter phy marks: "))
b = int(input("Enter eng marks: "))
c = int(input("Enter urdu marks: "))
d = int(input("Enter math marks: "))
e = int(input("Enter isl marks: "))
f = int(input("Enter bio marks: "))
g = int(input("Enter chem marks: "))
h = int(input("Enter s.s.t marks: "))

average_of_total(a,b,c,d,e,f,g,h)


# discovered myself 😉🤪
# we can make an empty parameter as well, inputs can be taken from the user using th fucntion, don't need to code again and again
def percent ():
    a = int(input("Enter phy marks: "))
    b = int(input("Enter eng marks: "))
    c = int(input("Enter urdu marks: "))
    d = int(input("Enter math marks: "))
    e = int(input("Enter isl marks: "))
    f = int(input("Enter bio marks: "))
    g = int(input("Enter chem marks: "))
    h = int(input("Enter s.s.t marks: "))

    marks = a+b+c+d+e+f+g+h
    total = int(input("Enter total: "))
    percent1 = marks/ total
    print(percent1*100)

percent()


# if we want that there is any default value, then we put that in this way
def call_product (b,a = 12): 
    print(a*b)

call_product(1)

# the function can't be in this way, the value that we want default that should be written later, otherwiswe, python will throw error

# def call_product (a = 12, b): 
#     print(a*b)

# call_product(1)


# return sends the value back so we can store or use it later
def call_product(b, a=12):
    return a * b

# Later we can print the returned value
add = call_product(1)
print(add)


# make a fucntion that prints the length of a list

cities = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Multan"]

def length_of_cities_list (cities):
    print(len(cities))


length_of_cities_list(["Lahore", "Karachi", "Islamabad", "Faisalabad", "Multan"])


def length_of_list (list1):
    print(len(list1))

length_of_list([10, "Lahore", 25.5, "Karachi", 100, "Islamabad", True, None])




fact = 1
for i in range (1 ,5+1 ):
    fact = fact *i
    print(fact)


n = 5
fact = 1
for i in range(1, 6):
    fact = fact * i 
print(fact)
    

def fact1 ():
    n = int (input("Enter number: "))
    fact = 1
    for i in range (1, n+1):
      fact = fact * i
      print(fact)
   
fact1 ()


#  usd to pkr converter
def converter (usd_value):
    print (usd_value, "dollars are equal to", usd_value*280,"pkr" )

converter (3)

def convert ():
       dollars = int(input("Enter total dollars in numbers: "))
       pkr = int(input("Enter current price of 1dollar in numbers: "))
       print(dollars, "is equal to",pkr*dollars,"pkr")
convert()


def number_checking():
    n = int(input("Enter a number: "))
    if (n % 2 == 0):
        print("you enter a \"EVEN\" number.")
    else:
          print("you enter a \"ODD\" number.")


number_checking()





### RECURSION ###                                  # RECURSION WITH RETURN VALUE

# BASIC RECURSION SYNTAX                          def function_name(n):
# def function_name(n):                               if condition:
#     if condition:                                      return value
#         return                                      return function_name(n - 1)
#     function_name(n - 1)


### PRINT RECURSION ###                           # SUM OF N NUMBERS (RECURSION)

# def function_name(n):                                     def function_name(n):
#     if n == 0:                                      if n == 0:
#         return                                          return 0
#     print(n)                                        return n + function_name(n - 1)
#     function_name(n - 1)


### FACTORIAL (RECURSION) ###

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n - 1)


### CORE RULE ###

# return work + function(n - 1)
# function calls itself with smaller value
# must have base condition




# def function_name(n):
#     if base_condition:
#         return base_value
#     return work + function_name(smaller_value)

def print_number(n):
    if (n == 0):
        return
    print(n)
    print_number(n-1)
    
print_number(5)


def print_number(n):
    if (n == 0):
        return
    print(n)
    print("end")  # we can add another statement after end of every recursion
    print_number(n-1)

print_number(5)



def sum (n):
    if (n ==0):
      return n
    
    return n +sum (n-1)

print(sum(7))



def sum (n):
    if n== 0:
        return n
    return n + sum(n-1)
   
print(sum(6))



def num (n):
    if n ==0:
        return
    print(n)
    num(n-1)
(num(4))



def num (n):
    if n == 0:
        return
    print(n)
    num(n-1)
print(num(4))




def num(n):
    if n <=3:
        return
    print(n)
    return num(n-1)
print(num(45))

# recurion is simply this, call the function in if loop, again and again, with one reducing number until the condition become false

def word (n):
  
    if n > 0:
        print("hello")
        word (n-1)
word(5)