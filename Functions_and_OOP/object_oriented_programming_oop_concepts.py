class student:
    clg = "Alpha"
    standard = "4th Grade"
    def __init__ (self, name, grade):
        self.name = name
# self.__grade = grade # use double underscores after self. to make your attribute private

s1 = student("Abrar", "A+")
print(s1)
print(s1.name)
# print(s1.__grade) this will give error beacause it has became partially private and can't be present in the output
print(s1.clg)

del s1 

## inheritane example, we can use info of one fucntion in the other
class student:
    clg = "Alpha"
    standard = "4th Grade"
    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade
    @staticmethod
    def welcome():
        print("Welcome to our portal")
s1 = student("Abrar", "A+")
print(s1)
print(s1.name)
print(s1.grade)
print(s1.clg)


class staff(student): # calling student class in staff class yto use student class data
       teahers_grade = "13th Grade"
       def __init__ (self, teachers_name, grade):
        self.name = teachers_name
        self.grade = grade

t1 = staff("Abrar", "A+")
print(s1)
print(t1.name)
print(t1.grade)
print(t1.clg) # we use attirbutes of other class in inheritance just like that's the part of our current class, using our current object name
t1.welcome() # same for functions, welcome fucntion is of student class but we use that in staff class as well using inheritance

# """
# types of inheritance
# single inheritance - single parent class single child class

# multiple-level inheritance - single parent class single child class, then we again make child class as parent class, then another class is made
#     (1. parent class) --> (2. child class) -(we will use 2nd class that is child class now)-> (3. child class) 
#      now we see 1 class was parent, 2 class was child, then we again make 3 class, as a child class of 2 and that's how 2 class become the parent of 3 class
#     in this the properties of our 1 and 2 class will be working in 3 class
#     this will be created as: 3 class name(2 class name), fucntion will be performed as 3 class(2 class (1 class))
#        # here we call 1 into 2 then 2 into 3
# multiple inheritance - two parent class one child class
#     1 class is made     2 class is made      3 class is made, it will have properties of both 1 and 2 class
#       # here we call 1 and 2 into 3 
# """
# example of multiple inheritance

class a:
        vara = "welcome to class a"
class b:
        varb = "welcome to class b"
class c(a , b):
        varc = "welcome to class c"

c1 = c()
print(c1.varc)
print(c1.varb)
print(c1.vara)

# here we can see that we call c class but use the data of a and b class also


class student:
    def __init__ (self, name):
        self.name = name
    @staticmethod
    def welcome():
        print("Welcome to our portal")

class staff(student):
     def __init__(self, name, grade):
         self.grade = grade
         self.name = name

         super().__init__(name)
    
          

s1 = staff("bushra", 23)
print(s1.name)
s1.welcome()

t1 = staff("rida", 16)
print(t1.grade)
print(t1.name)
t1.welcome()




class student:
    clg = "Alpha"

    @classmethod
    def clg_name(cls):
         cls.clg = "Hope"
         print(cls.clg)
print(student.clg_name())


# @staticmethod --> use when no method of class or init, we dont want to use
# @classmethod (cls)--> use when only we want to use class attributes
# @instancemethod (self) --> use when we want to use instance properties

# using super method and class method
class car:
     company_name = "mercedes"
     model = 2026
     def __init__(self, month, color, category):
           self.month = month
           self.color = color
           self.category = category

class bike(car):
    def __init__(self, month, color, category, clutches):
        self.clutches = clutches
        super().__init__(month, color, category)
    @classmethod
    def change_company_name(cls):
        cls.company_name = "Prada"
        print(cls.company_name)

r1 = bike("january", "blue", "bike", "5")
print(r1.month)
print(r1.color)
print(r1.clutches)
print(r1.model)
print(r1.company_name)
print(r1.category)
print(bike.company_name)
bike.change_company_name() # to print cls call that fucntion, printing statement should be in the function



class car:
     company_name = "mercedes"
     model = 2026
     def __init__(self, month, color, category):
           self.month = month
           self.color = color
           self.category = category

r1 = car("january", "blue", "bike")
print(r1.month)
print(r1.color)
print(r1.category)
r1.color = "yellow" # to change something in our object, we can do like this
print(r1.color)

class student:
    def __init__(self, phy,comp, math):
        self.phy = phy
        self.comp = comp
        self.math = math
        self.percentage = ((self.phy + self.comp + self.math)/3)
    def percent(self):
        self.percentage = ((self.phy + self.comp + self.math)/3)
        print(self.percentage)



s1 = student(33, 43, 54)
print(s1.phy)
print(s1.math)
print(s1.comp)
print(s1.percentage)
s1.phy = 89 # chnage the value of object
print(s1.phy)
s1.percent() # need function to print the changed value, can't be print print(s1.percentage) like this, if we do, output will be according to previous data not upadated

  # for doing the same this thing we have property method


class student:
    def __init__(self, phy,comp, math):
        self.phy = phy
        self.comp = comp
        self.math = math
    @property
    def percent(self):
        return ((self.phy + self.comp + self.math)/3) # we need to return the value, can't use print here

s1 = student(33, 43, 54)
print(s1.phy)
print(s1.math)
print(s1.comp)
print(s1.percent)
s1.phy = 89
print(s1.percent) # just do as usual, updated output will come



class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def shownumber(self):
         print(self.real,"i" ,"+", self.img,"j")

    def __add__(self, other):
         n1 = self.real + other.real
         n2 = self.img + other.img
         return complex(n1, n2)
    
num1 = complex(1,3)
num1.shownumber()

num3 = num1 +num1 # this is possible because we use dunder function __add__ 
num3.shownumber()



class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def shownumber(self):
         print(self.real,"i" ,"+", self.img,"j")

    def __sub__(self, other):
         n1 = self.real - other.real
         n2 = self.img - other.img
         return complex(n1, n2)
    
num1 = complex(1,3)
num1.shownumber()

num3 = num1 - num1 # this is possible because we use dunder function __sub__ 
num3.shownumber()







class Person:
    def __init__(self, age):
        self.name = []
        self.age = age
        self.version = []
p1 = Person("23")
p1.name = "Rida"
b = p1.__dict__   # tells about which variables are set using self.
print(b)
a = p1.__dict__ [__name__]= "12"   # change any data for object
print(a)
print(p1.age)
p1.name = "Rida"
print(p1.name)

print(help (Person)) # tells about soemthing all dataa




# In method overriding, the child class redefines the same method that already exists in the parent class.
# The conditions are:

# Same method name 
# Same parameters (normally) 
# Different implementation/body 

class parent:
    def hello(self):
        print("hello")


class child(parent):
    def hello(self):
        print("hi")
    
a = parent()
a.hello()
b = child()
b.hello()



class Parent:
    def calculate(self, a, b):
        print(a + b)


class Child(Parent):
    def calculate(self, a, b):
        print(a - b)


p = Parent()
p.calculate(10, 5)

c = Child()
c.calculate(10, 5)



# guideline about variables for class

# Use parameters for the input the method needs (book, name, price).
# Use local variables for temporary calculations (index, total, found).
# Use instance variables (self.) to store or update the object's state (self.books, self.balance).
# Use class variables only for values that should be the same for every object (company_name, tax_rate, library_name).





