######## D I C T I O N A R Y ########
# this is a dictionary syntax
# dictionary_name = {                     student = {
#       key1: value1,                     "name": "Alice",
#       key2: value2,        e.g:         "age": 20,                                   
#       key3: value3                      "grade": "A"
#      }                                   }                

info = {
    "name" : "rida",
    "age" : 35,
    "sub" : ["Eng", "math", "phy"]
}

print(info)  # if we want to print our whole dictionary
print(info["name"])  # if we wnat to get some special key of our dictionary, this methods can be used
print(info["age"])
              


info["name"] = "zain"     # to change some value in dtictionary  
print(info)

info["surname"] = "shah"  # with same method we can add any key which we want
print(info)

info["number"] = 23
info["list1"] = [1, 2, 3]

print(info)


dict2 = {}  #empty dictiioanry can be made
# and can store values and keys later in it

dict2["names"] = ["zain", "kashif"]
print(dict2)



# this is a nested dictionary syntax
# dictionary_name = {                           students = {
#     outer_key1: {                                 "student1": {
#         inner_key1: value1,                           "name": "Alice",
#         inner_key2: value2,                           "age": 20
#     },                                e.g;          },
#     outer_key2: {                                 "student2": {
#         inner_key1: value3,                           "name": "Bob",
#         inner_key2: value4                            "age": 22
#     }                                             }
# }                                                }

dict3 = {
    "name" : "rahul", 
    "subjects" : {
        "phy" : 97,
        "math" : 89,
        "eng" :79
    }
    
}


print(dict3) #if we want to print whole dictionary
print(dict3["subjects"])  # if we want to print just some specific part of dictionary
print(dict3["subjects"]["phy"]) # if we want to print specific data from our nested dictionary


dict3 = {
    "name" : "rahul", 
    "subjects" : {
        "phy" : 97,
        "math" : 89,
        "eng" :79
    },
  "age" : {
       "sister" : 12,
       "brother" :23
   }
}

print(dict3 ["age"]["brother"])


dict3.keys() # when we want to get all the keys of our dictionary, only can get main keys, not nested keys
print(dict3.keys())


list(dict3.keys()) # we can type cast out dict data, like if we want to print that in other form except this : dict_keys(['name', 'subjects', 'age'])
print(list(dict3.keys())) 
print(tuple(dict3.keys()))

len(dict3) # to print how many keys a dictionary contain
print(len(dict3))

print(len(list(dict3.keys()))) #puting a layer, both above step in one step



dict3.values() # to get all values of a dictionary, calue is te data that we store in a key
print(dict3.values())


print(list(dict3.values())) # can be printed in the form of list or tuple as well
print(tuple(dict3.values()))


dict3.items() # give us all the data in the form of pairs, 1st key will have pair with 1st value and so on
print(dict3.items())
print(list(dict3.items()))
print(tuple(dict3.items()))


# we can access a specific key, by making new variable

a = list(dict3.items())
# we can't write in this way, this should be in the form of list cause dictioanry has don't array method
# a = dict3.items()
print(a[0])
print(a[2])


dict3.get("our Key") # get the value of a sepcific key
print(dict3.get("name")) #if we put any key that doesn't exist, it will not show error, simply print none
print(dict3["name"]) #if we put any key that doesn't exist, it will show error

# print(dict3.get("name1")) --> print None
# print(dict3["name1"]) --> shows error


dict3.update({"key" : "value"}) # use to add something in our original dictionary
print(dict3.update({"internsip" : "no"}))  # this will give none to us, dictionary will not be printed
print(dict3)

# we can save update multiple values or keys by using update method
print(dict3.update({"internsip" : "no", "age1" : "23"})) # this will give none to us, dictionary will not be printed
print(dict3)

# if we accidently add the exisiting key in our update dictionary, the existing key's value will be overwrite
print(dict3.update({"internsip" : "no", "age" : "23"})) # this will give none to us, dictionary will not be printed





######### S   E   T #########

# in set all kind of data type can be stored except list and dictionary, because these are mutable and set is always consist on immutable values
# important point, the set is mutable, but the items or element in it are immutable

set1 = {1, 2, 3, 8.7, 45.3, "hello", "23", (1, 23, "his")}
print(set1) 

set2 = {1, 2, 3, 8.7, 9.0, 8.7} # duplicate values will be ignored, no error will come
print(set2)

print(len(set1)) # no. of itmes

set3 = set() # an empty set is created this way
print(type(set3))
print(set3)


set1.add("element") # add new value
print(set1.add("2323"))
print(set1)

set1.remove(1) # use to remove a value from set
print(set1)


set1.clear() #clear the set
print(set1)


set2.pop() #print a random value
print(set2.pop())

set1 = {1, 2, 3, 8.7, 45.3, "hello", "23", (1, 23, "his")}
set2 = {1, 2, 3, 8.7, 9.0, 8.7}
set1.union(set2) #combine both set values and return a new set
print(set1.union(set2))


set1.intersection(set2) # get common values in both sets
print(set1.intersection(set2))

#### solving problems #####


# 1. Store the following word meanings in a Python dictionary:
# table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"

new_dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture",
        "list of facts and figures"]
        
}

print(new_dict)


# 2. You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students?
#     {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
new_set = {"python", "java", "c++", "pyhton", "javascript", "java", "python", "java", "c++", "c"}
print(len(new_set)) 



# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
dict = {}

a = int(input("Enter marks: "))
b = int(input("Enter marks: "))
c = int(input("Enter marks: "))

d = input("Enter subject name: ")
e = input("Enter subject name: ")
f = input("Enter subject name: ")

dict.update({d : a})
dict.update({e : b})
dict.update({f : c})

print(dict)


# Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
set = {9 , "9.0"}
print(set)
