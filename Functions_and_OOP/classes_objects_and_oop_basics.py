# class ClassName:
#     def function_name(self, parameter):
#         self.variable = parameter


class student:      
    name = "Karan"    # all the students in this class will have name Karan

s1 = student()
print(s1)  # print the object, Here is the object. It belongs to the student class, and this is its memory address

s1 = student()
print(s1.name)  # print the name of 1st obeject


s2 = student()
print(s2.name)  # print the name of 2nd obeject


class car:
    color = "Black"
    brand = "mercedes"
    price = "1 million+"

car1 = car()
print(car1.color)
print(car1.brand)
print(car1.price)




class student:  
    def __init__(self, new_name):
        self.first = new_name
        print(self)
        print("add new student") 
    name = "Karan" 

s1 = student("Farhan")
print(s1.first)

s2 = student("ayesha")
print(s2.first)




class student:  
    college = "ABC "  # the info that is same for every object will be written like this
    name = "anaonmyous"

    def __init__(self, new_name):
        self.first = new_name   # with self we define that the information of every object will be diferent
        print(self)
     

s = student("Ali")
print(s.first) 

s1 = student("Farhan")
print(s1.first)

s2 = student("ayesha")
print(s2.first)
print(s2.college)  # print statement like this above init function, otherwise there will be error
print(s2.name)
# s4 = student()  # this is wrong method to print college, because pyhton would rquire an argument here, so we can print college with our already exisiting object
# print(s4.college)


class student:  
    college = "ABC "  
s4 = student()
print(s4.college)   # this method is correct because there is no init fucntion here


# Code                   	Meaning
# self.first = new_name	    store value in object
# student("Karan")  	    give value
# print(s.first)	        show stored value




class student:  
    college = "ABC "  # the info that is same for every object will be written like this
    name = "anaonmyous"

    def __init__(self, new_name, classes):
        self.first = new_name    # with self we define that the information of every object will be diferent
        self.second = classes
        print(self)
        print("student data")
a = student("aryan", "1st class")
print(a.first)
print(a.second)
print(a.college)


b = student("",classes="2nd class")  # this will print our fucntion data

# init fcuntion is a constructor, is it basically for initializing an object mean if we want to add some info for specific object for that init/constuaction fucntion will be used.
# if we don't create it ourslef, pyhton will create it itself

class student:  
    college = "ABC "  # the info that is same for every object will be written like this
    name = "anaonmyous" # class attributes
    total = 505
    def __init__(self, new_name, classes):
        self.first = new_name    # with self we define that the information of every object will be diferent
        self.second = classes # object attributes
        
    def welcome(self):  # method function
        print("welcome students")
    
    def marks(self,a, b):
        print("the sum is", a+b)

a = student("aryan", "1st class" )
print(a.first)
print(a.second)
print(a.college)
print(a.total)
a.welcome()
a.marks(67,89)

b = student("Bushra","4th Grade")
b.welcome()
b.marks(23,80)


class student():
    def __init__(self, name, subject1, subject2,subject3):
        self.name = name
        self.mark1 =  subject1
        self.mark2 = subject2
        self.mark3 = subject3
    def average(self):
       a = self.mark1 +self.mark2 +self.mark3
       b= a/3
       print ("The average is", b)

student1 = student("Rida", 23,43,54)
print(student1.name)
student1.average()


student2 = student("Zain", 29,55,94)
print(student2.name)
student2.average()




class Account():
    def __init__ (self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        

    def debit(self): # i use here static method or try to craete a new varibale, simply we can use self to get the access to init fucntion in method fucniton
        a = int(input("Enter amount you want to add: ")) # the mistake i made, i gorget self, self is important cause if we want to add or make other change in init function, self is important in method function
        self.balance = self.balance +a
        print("Your total balance is: ", self.balance)
              
    def credit(self):
        a = int(input("Enter amount you want to get: "))
        self.balance = self.balance  - a
        print("Your total balance is: ", self.balance +a)
    
    def tb(self):
        print("Current balance is: " , self.balance)


dbt = Account(10000, 363931220139072466402)
dbt.debit()
dbt.credit()
dbt.tb()



class Account():
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self):
        amount = int(input("Enter amount to withdraw: "))
        self.balance = self.balance - amount
        print("Balance is", self.balance)

    def credit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance = self.balance + amount
        print("Balance is", self.balance)

    def print_balance(self):
        print("Current balance is", self.balance)


balance = int(input("Enter your balance: "))
account_no = int(input("Enter your account number: "))


acc = Account(balance, account_no)
acc.credit()
acc.debit()
acc.print_balance()





class Person:
    def __init__(self, age):
        self.name = []       # Create an instance variable 'name' with a default empty list. This allows us to create objects without passing a name initially.
        self.age = age     # Store the age passed during object creation.


# Create the first object.
p1 = Person("23")
print(p1.age)  # Print the age.
p1.name = "Rida"  # Assign a name later. # Since 'name' already exists as an instance variable # we can update it whenever we want.
print(p1.name) # Print the updated name.

 
# Create another object.
p2 = Person("24")

print(p2.age)  # Print the age.
print(p2.name) # We did not assign a name to p2.
# This does NOT cause an error because 'name' was already
# initialized in __init__. It still exists and contains
# its default value (an empty list).

# simple define below

class Person:
    def __init__(self, age):
        self.name = []  # we can make a instance variable like this, if we don't want to keep an argument for every object
        self.age = age
    
p1 = Person("23")
print(p1.age)
p1.name = "Rida" # then add data in that like this
print(p1.name) # print like this

p2 = Person ("24")
print(p2.age)
# skipping name portion accoridng to our will, won't make error


