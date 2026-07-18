for k in range (5):
    print(k + 1)

for k in range (1 , 9):
    print(k)


for k in range ( 5 ):
     print (k)


#       L O O P S          #


#   for loops

#      for variable in sequence:
#            statement

abc = ("a", "b", "c")
for letters in abc:
    print(letters)


#      for number in range(start , end):
#             statement

for numbers in range (10):
    print(numbers)


#     for variable in range(stop):
#          statement

for m in range(8):
     print(m)


#    for variable in range(start, stop):
#        statement

for o in range ( 20 , 2000):
      print(o)


for o in range ( 20 , 2000):
      print(o+1)



#     for variable in range(start, stop, step):
#            statement
#step = how far to jump each iteration.

for q in range(12, 23, 2):
     print(q)



#       while (condition):
#             statement
#             increment/decrment(optional according to need)
er = 0
while(er < 10):
    print(er)
    er = er +1

er = 0
while(er >= 10):
    print(er)
    er = er +1

i = int(input("Enter the number:"))
while (i <= 40):
     i = int(input("Enter the number:"))
     print (i)



op = 1
while op <= 10:
    print(op)
    op += 1
#code i write
# op = 10
# while(op >= 10):
#      print(op)
#      op = op + 1



for even in range (2, 20, 2):
   print(even)
#correct 


table = int(input("Enter table number: "))

for i in range(1, 11):
    print(table * i)
# code i write
# table = int(input("Enter table number:"))
# for table in range(1,10):
#      table2 = table*1
#      print(table2)
#      table2 = table2 + 1

for i in range(10, 1, -1):
    print(i)
#correct

num = int(input("Enter number:"))
while(num != 0):
    print(num)
    num = int(input("Enter number:"))
#correct


num = int(input("Enter number:"))
while(num != 0):
    print(num)
    num = int(input("Enter number:"))


num = int(input("Enter number:"))
while(num != 0):
    print(num)
    num = int(input("Enter number:"))
else:
    print("i am in else loop")



for i in range(1 ,12):
     print("5 X",i , "=", 5*i)
     if(i == 10):
         continue



for i in range(1 ,12):
     print("5 X",i , "=", 5*i)
     if(i == 10):
         break
     

i = 1
while (i <= 10):
    print(i)
    i = i+1
    if( i ==7):
        break


for h in range (1, 11):
    print(h)
    if(h ==6):
        break



for table in range (1, 11):
    print("7 x " ,table, "=" , 7 *table )
    if (table == 5):
        break



for i in range(1, 12):
    print(i*9)
    if(i == 10):
        break
        


for i in range(1, 12):
    print(i*9)
    if(i == 10):
       continue



#emulate do while loop
i = 1
while True:
    print(i*2)
    i = i + 1
    if (i==3):
        break