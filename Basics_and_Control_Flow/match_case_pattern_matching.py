
day = int(input("Enter 1st Number: \n"))
match day:
    case 1:
        print("Monday")
  
    case _:
        print("You enter another day.")


color = input("Enter traffic light colors:").strip().lower()
match color:
    case "red":
        print("Stop.")
    case "green":
         print("Go.")
    case "yellow":
        print("Get ready to go.")
    case _:
        print("You enter invalid color")
