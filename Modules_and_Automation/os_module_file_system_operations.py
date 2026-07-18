import os

os.mkdir("data") # make a folder

for i in range (0, 100):
    os.mkdir(f"data/day{i+1}") # make folders 
    os.rename((f"data/day{i+1}") ,(f"data/tutorial{i+1}") )  # mrthod to rename a folder


import os
a = os.listdir("data")
print(a)

for folder in a:
    print(folder)




import os
os.getcwd() # tells in which directory we are
print(os.getcwd())


os.chdir("D:\Python Files\_folder1")  # use to change the path pf the directry
print(os.getcwd())


os.listdir() # shows everything in the foldere
print(os.listdir())


os.mkdir("New_Folder") # creates new folder


os.makedirs("Python/Files/Projects") #create folder in folder


import os
os.rename("Python", "New_Folder2")  # reaname folders, main or sub folder does not matter, old folder name come before, new one come later


import os
os.rmdir("New_Folder") # delete empty folder


import os
os.remove("ChatGPT Image.png")  # delete a file


import os
print(os.path.exists("D:\Python Files\_folder1")) # check if the given path exist or not


import os
os.path.isfile("main.py") # check if given path is file or not
print(os.path.isfile("main.py"))


import os
os.path.isdir("New_Folder")
print(os.path.isdir("New_Folder"))

import os
os.path.join("Users", "Window", "Files") # create automatically path instead of doing manually
print(os.path.join("Users", "Window", "Files"))


import os
os.environ.get()  # gives all environment variables


import os
os.environ["COURSE"] = "Python"  # create ypur own environment variable
print(os.environ.get("COURSE"))


# create many folders at once using os
import os
for i in range(11):
    os.mkdir(f"Day{i}")

    