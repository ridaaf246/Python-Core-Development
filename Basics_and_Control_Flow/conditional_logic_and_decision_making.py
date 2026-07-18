a = int(input("enter your age: "))
print("Your age is", a)

if (a>18):
    print("you can drive")
else:
    print("You can't drive")


print(a==14)
print(a<=18)
print(a>=18)
print(a!=18)

#conditional operators
# !=  Not equal
# == Equal
# <= less than or equal
# >= greater than or equal


a = int(input("Enter your age: "))
print("Your age is", a)

if (a>=18):
    print("You can drive")
    print("congratulations")
    print("Have safe drives!")
else:
    print("You can't drive")
    print("The problem is your age not you")
    print("Best luck for next time!")

#you can't write any statement after before else except they are loop statements, loop structure breaks
print("loop printed")
print("checked all")


apple = int(input("Enter how many kg of apples you want to buy: "))
budget = int(input("What is your budget?"))

if(apple*300 <= budget):
     print("You can buy the apples, go ahead!")
else:
    print("Your budget doesn't meet your requirement")
    print("Wish you best for the next time!")


apple_price = 800
budget1 = int(input("Enter of how much money you want to buy apples\n"))

if(apple_price == budget1):
      print("Robots are packing your apples." \
      "Please stay with us, don't leave your position.\n" \
      "Thanks for grocery from our store")
elif(apple_price > budget1):
     print("Your budget is less to buy the apples." \
     "Better try for next time.")
elif(apple_price < budget1):
     print("Robots are packing your apples." \
      "Please stay with us, don't leave your position.\n" \
      "Thanks for grocery from our store")
     print("Kindly take your remaning",int(budget1 - apple_price), "from your the machine on yourleft side")
else:
     print("You enter invalid data")





num = int(input("Enter number: "))

# First main branch: valid or invalid range
if num < 0 or num > 60:
    print("Invalid number! Not in range 0 to 60.")

else:
    print("Number is in valid range (0 to 60).")

    # Second branch: upper half or lower half
    if num >= 40:
        print("Number is in upper range (40 to 60).")

        # Third branch: detailed classification
        if num >= 41 and num <= 45:
            print("It is between 41 and 45")

        elif num >= 46 and num <= 50:
            print("It is between 46 and 50")

        elif num >= 51 and num <= 55:
            print("It is between 51 and 55")

        elif num >= 56 and num <= 60:
            print("It is between 56 and 60")

    else:
        print("Number is in lower range (0 to 39).")

        # Lower range breakdown
        if num >= 30 and num <= 39:
            print("It is between 30 and 39")

        elif num >= 20 and num <= 29:
            print("It is between 20 and 29")

        elif num >= 10 and num <= 19:
            print("It is between 10 and 19")

        elif num >= 0 and num <= 9:
            print("It is between 0 and 9")





marks = int(input("Enter your marks: \n"))

if marks < 0 or marks > 100:
    print("You entered invalid number.")

else:
    if marks >= 80:
        if marks >= 90:
            print("Excellent Performance")
        else:
            print("Very Good Performance")

        print("Your grade is 'A'")

    elif marks >= 60:
        print("Great, Your grade is 'B'")

    elif marks >= 40:
        print("Good, Your grade is 'C'")

    else:
        print("Best luck for next time, Your grade is 'F'")