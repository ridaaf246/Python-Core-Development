# list is a mutable data type, things can be changes or add

# # # L I S T  M E T H O D S # # #

list1 = []
# we can make an empty list

list1 = [1, 2, 3, 4]
print(list1)
list1.append(5)# add new element at the end of list list, just one element can be added 
print(list1)    # and when we print again, we will get list with new addition

list1 = [4, 3, 1, 2]
print(list1)
list1.sort() # arrange the values in assending order
print(list1)   # when we run this, it will give None output, it directly add the correct order in the varibale


list1 = [4, 3, 1, 2]
print(list1)
list1.sort(reverse = True) # arrange the values in decending order
print(list1)   # when we run this, it will give None output, it directly add the correct order in the varibale

# same methods are possible fro string as well

list1 = ["apple", "guava", "coconut","banana"]
print(list1)
list1.append("litchi")# add new element at the end of list list, just one element can be added
print(list1)    # and when we print again, we will get list with new addition


list1 = ["apple", "guava", "coconut","banana"]
print(list1)
list1.sort() # arrange the values in assending order
print(list1)   # when we run this, it will give None output, it directly add the correct order in the varibale, it will give according to alphabetical arrnagement


list1 = ["apple", "guava", "coconut","banana"]
print(list1)
list1.sort(reverse = True)# arrange the values in decending order
#_________(reverse is a function part not a specific variable we again make)
print(list1)   #when we run this, it will give None output, it directly add the correct order in the varibale


list1 = [4, 3, 1, 2]
print(list1)
list1.reverse() #reverse the order of the list
print(list1) # and when we print again, we will get list in reverse order

# new methods

list1 = [1, 2, 3, 4]
print(list1)
list1.insert(2,9) # insert a new element at a specific index
# ___._____(index number at which we want to add, element to whcih we want to change)
print(list1) # and when we print again, we will get list with changed element


list1 = [1, 2, 4, 3, 4]
print(list1)
list1.remove(4) # remove the specific element from the list, if we have same two elements, it will find first one and remove
# ___.______(element that we want to remove)
print(list1) # and when we print again, we will get list with changed element


list1 = [1, 2, 4, 3, 4]
print(list1)
list1.pop(2) # remove the element at specific index from the list
#____.__(index number from where we want to remove the elemnt)
print(list1) # and when we print again, we will get list with changed element


# if any of these methods, suppose fuction is like this
list1 = [4, 3, 1, 2]
print(list1)
print(list1.reverse())
# we will get none in our output, value will be directly stored in the variable




# # T U P L E # #
# tuple is a immutable data, nothing can be chnaged


tup1 = (1, 2, 3, 4)
print(tup1[0])
print(tup1[3])

tup1 = ()
print(tup1)
# we can create an empty tuple

tup1 = (1,) # we can store one single element in tuple with coma, without comma it will be consider as int, float or stiring not a tuple
print(tup1)
print(type(tup1))

tup1 = (1)
print(type(tup1))

tup1 = (1.89)
print(type(tup1))

tup1 = ("1")
print(type(tup1))

tup1 = (1, 2, 3, 4)
print(tup1.index(2)) # it tells that at which index specific element exists
# _____________(elment whose index we want to know)


tup1 = (1, 2, 3, 4)
print(tup1.count(2)) # tells how many times a element in present in a tuple
# _____________(that element about which we want to know)

tup1 = (31, 52, 345, 44, 31,31)
print(tup1.count(31))


movies = []

a = [input("Enter 1st movie name:")]
b = [input("Enter 2nd movie name:")]
c = [input("Enter 3rd movie name:")]

movies.append(a)
movies.append(b)
movies.append(c)

print(movies)


list1 = [1, 2, 1]

c = list1.copy()
c.reverse()
if (list1 == c ):
    print("palandrome")
else:
    print("no")


tupx = ("c", "d", "a", "a", "b", "b", "a")
print(tupx.count("a"))


tupx = ["c", "d", "a", "a", "b", "b", "a"]
tupx.sort()
print(tupx)
