# Reading Mode ("r") - Read the entire file

file = open("new.txt", "r")   # Open the file in read mode
data = file.read()            # Read the complete file
print(data)                   # Print the file content
file.close()                  # Close the file


file = open("new.txt")        # Can be like this, cosidered as read mode by default
data = file.read()            # Read the complete file
print(data)                   # Print the file content
file.close()



# Read only the first line using readline()

file = open("new.txt", "r")
data = file.readline()        # Read the first line only
print(data)

file.close()


# Read the file line by line
# Each call to readline() reads the next line.

file = open("new.txt", "r")

data1 = file.readline()       # First line
print(data1)

data2 = file.readline()       # Second line
print(data2)

data3 = file.readline()       # Third line
print(data3)

data4 = file.readline()       # Fourth line
print(data4)

file.close()


# Write Mode ("w")
# Creates a new file if it doesn't exist.
# If the file already exists, all previous data is deleted.

opening_file = open("new.txt", "w")
opening_file.write("Hello, how are you? Hi, I am good.\n")
opening_file.close()


# Append Mode ("a")
# Adds new data at the end of the file without deleting
# the existing content.

opening_file = open("new.txt", "a")
opening_file.write("Hi, what's up? How are you? Hi, I am good.")
opening_file.close()


# Create a new file using Write Mode

i = open("hello.txt", "w")
i.write("Hello, made this new file.")
i.close()


# Append and Read Mode ("a+")
# - Appends data at the end of the file.
# - Also allows reading the file.
# - Creates the file if it doesn't exist.

i = open("hello.txt", "a+")
i.write(" Hello, made this new file using append mode.")
i.close()


# Write and Read Mode ("w+")
# - Deletes all previous data.
# - Writes new data.
# - Also allows reading.

i = open("hello.txt", "w+")
i.write("Hello, made this new file using write mode.")
i.close()


# Using "with open()"
# The file is automatically closed after the block finishes.
# No need to call close().

with open("new.txt", "r") as fp:
    file = fp.read()

print(file)


# Delete a file using os.remove()

import os

os.remove("hello.txt")


# Create a practice file and write multiple lines

new = open("practice.txt", "w")
new.write("Hi everyone\n")
new.write("We are learning File I/O\n")
new.write("using Java\n")
new.write("I like programming in Java")

new.close()


# Replace "Java" with "Python"

with open("practice.txt", "r") as new:
    file1 = new.read()

# Replace every occurrence of "Java" with "Python"
updated_data = file1.replace("Java", "Python")

print(updated_data)


# Save the updated content back into the file

with open("practice.txt", "w") as new:
    new.write(updated_data)


# Search for a word in the file
# find() returns:
# - Index number if the word exists.
# - -1 if the word is not found.

with open("practice.txt", "r") as new:
    file = new.read()

    if file.find("learning") != -1:
        print("Found")
    else:
        print("Not Found")





