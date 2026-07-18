names = "Rida Fatima"

#syntax
#variable name[start:end]
#starting chaarcter prints : ending character does not print(the character before to it prints)

print(names [0:5])

length = len(names)
print(length)


print("my name is", length, "letter long")


fruit = "watermelon"
print(fruit[0:3])
#print from 1st character to 3rd characrer


length_of_fruit = len(fruit)
print(length_of_fruit)

print(fruit [:])
#work only for STRINGS, we can't use here varibale length_of_fruit, python automatically consider zero on left side and the number of last character in the variable on right side of the  of colon and print characters from start to end

print(fruit [:5])
##work only for STRINGS, we can't use here varibale length_of_fruit, python automatically consider zero on left side of the  of colon and print characters from start to array 5


print(fruit[-1 : -3])
#Minus means count from the end of the string
#prints the chatracters to oppostie side
#need to keep in mind interger scale

print(fruit[-6 : -3])

print(fruit[-8:-2])

nm = "harry"
print(nm[-4:-2])
#output is ar

