
# | Syntax                                    | Use                                 | Example                     |
# | ----------------------------------------- | ----------------------------------- | --------------------------- |

# | mport module                              | Import the whole module             | import math                 |
 
# | import module as alias                    | Import with a shorter name          | import numpy as np          |

# | from module import function               | Import only one function            | from math import sqrt       |

# | from module import function1, function    | Import multiple functions           | from math import sqrt, pi   |

# | from module import                        | Import everything (not recommended) | from math import            |


import math   # Import the whole module 
print(math.sqrt(23))


import time
print(time.localtime()) # method to import local time
print(time.localtime().tm_hour) # method to import local time and print just hour
print(time.localtime().tm_min)  # method to import local time and print just minute and so on


import time as t # Import module with a shorter name (rename module for youe ease)
print(t.localtime().tm_min)


import math as m
print(m.sqrt(23))


from math import sqrt  # Import only one specific function from module
print(sqrt(2))


from math import sqrt, factorial # Import multiple functions from a module
print(sqrt(2))
print(factorial(5))

 
from math import *  # Import everything from a module, causes ease because just write fucntion, don't need to write module name (math.sqrt(5)❎ sqrt(5)✅)
# not recomended because if we import multiple modules, and any of these have same functions that can cause issues in program
print(sqrt(6))
print(pi)
print(log(68))

from math import sqrt as s  # rename fucntion
print(s(34))

from math import sqrt as a, factorial as b  # import multiple fucntions with differnet alias in one statement
print(a(23))
print(b(23))

import math
print(dir(math)) # using dir we can print all the functions that exist in module

import math
print(dir(math.nan))



# import function from another file as a module
# make a file, do programming in that
# using this method we can import or use that in our another file
from python_main_module_and_execution_control import welcome, a, b
import python_main_module_and_execution_control
welcome()

from python_main_module_and_execution_control import *  # import complete other file


# Import the sleep() function from the time module, wait for 3 seconds, then print "Done!".

import time
print(time.sleep(3))  
print("Done")

import time
time.sleep(3)
print("DONE")


# Import choice() from the random module and randomly select one fruit from a list.

from random import choice
fruit = (["banana", "orange" , "apple"])
a = choice(fruit)
print(a)


# Import the factorial() function with the alias fact and print the factorial of 8.

from math import factorial as fact
print(fact(8))


from random import choice
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = choice(list)
print(a)

