a = "Rida Fatima"

print(a)
print(a.upper())
print(a.lower())
#convert string to upper and lower case


b = "Rida Fatimaaaaaaaaaaaaaaaaaaaaaa"
print(b.rstrip("a"))
#remove the character from the right side only if the given character in on the last, not in middle or start


c = "!!!!!!!!rida!!!!"
print(c.rstrip("!"))


b = "Rida Fatima"
print(b.rstrip("a"))


b = "Rida Fatima"
print(b.rstrip("i"))


b = "Rida Fatimaaaaaaaaaaaaiiiiii"
print(b.rstrip("a"))


b = "Rida Fatimaaaaaaaa"
print(b.rstrip("t"))


c = "!!!!!!!!rida!!!!rida"
print(c.replace("rida" , "eman"))
#repalce the string wiwth other string)


d = "rida fatima is a girl"
print(d.split(" "))
#make a list of string after every character you choose

d = "rida fatima is a girl"
print(d.split("a"))

d = "rida fatima is a girl"
print(d.split("m"))


f = "learning python to have a skill"
print(f.capitalize())
#capitalize the first character of a string

f = """learning python to have a skill.
i hope, i will have advantage of it in future.
my skill and ai togetehr will be amazing"""
print(f.capitalize())


f = """Learning pYthon to have a skill.
i hope, i Will Have advantage of it In future.
My skill and ai togetehr will be AMAZing"""
print(f.capitalize())


str1 = "welcome to learning python"
print(str1.center(80))
#add empty spaces to your string

d = "everything is amazing"
print(d.count("a"))
#tells how many time a character or word is present in a string

d = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing"
print(d.count("is"))

g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
print(g.endswith("!"))
#tells that our string wether ends with that character specific character

g = "there was all great things," \
"we enjoy a lot"
print(g.endswith("t"))
#if it is ending, we will see true in our output, if it's not we will see false in our output


g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
print(g.find("is"))
#tells at which index your character is present, just for first one index not others

g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
print(g.find("b"))
#tells that how many times a character or word is present in string, gives -1 if we on't have that character or word in our string


g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
print(g.find("i"))
#similar to find

g = "everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing" \
"everything is amazing!!!!" \
"there was all great things," \
"we enjoy a lot"
#print(g.index("b"))
#but shows error if that charcter or word is not found instead of -1


s = "welcome to this world"
print(s.isalnum())
# used to check whether a string contains only letters and numbers
# True - if the string has only A–Z, a–z, or 0–9
# False - if it contains spaces, symbols, or punctuation

# f = "232424"
# print(f.isalnum())
#isalnum works only on strings, it shows error

f = "232424"
print(f.isalnum())


f = "abcdef"
print(f.isalnum())


f = "abc5372"
print(f.isalnum())

f = "adcn!d434"
print(f.isalnum())

f = "abc 435 number %"
print(f.isalnum())


s = "welcometothisworld"
print(s.isalpha())
#check whether a string contains only letters
#True only if the string has only A–Z, a–z
#False,if it contains numbers, spaces, symbols, or punctuation

s = "welcome to this world"
print(s.isalpha())

s = "welcometothisworld00"
print(s.isalpha())

s = "welcome_to_this_world"
print(s.isalpha())


s = "welcome to this world"
print(s.islower())
#use to check wether chracters in the string are in lower case, does not bother the number, space, symbol or puntuations
#gives true if all are lower case, every single caharters needs to be lower case to be true
#gives false if upper case is found

s = "Welcome To This World"
print(s.islower())

s = "welcome to this world00"
print(s.islower())

s = "welcome to this @ world00"
print(s.islower())


s = "Welcome To This World"
print(s.isprintable())
#shows true if all the chracters of the strings are printable
#shows false if any character of the string is not printable

s = "Welcome To This World\n"
d = "you will enjoy this palce"
print(s.isprintable())
# \n is not printable, output will be flase

s = "           "
print(s.isspace())
#gives true only if we have only space in our string

s = "     sd      "
print(s.isspace())
#it will gives false


s = "Welcome To This World"
print(s.istitle())
#gives true onyl if all first characters of all words in a string are capital

s = "Welcome to this world"
print(s.istitle())
#otherwise returns false


s = "Welcome to this world"
print(s.isupper())
#use to check wether chracters in the string are in uppercase, does not bother the number, space, symbol or puntuations
#gives true if all are upper case, every single caharters needs to be upper case to be true
#gives false if lower case is found


s = "Welcome to this world"
print(s.startswith("Welcome"))
#gives true if string is starting with your given string

s = "Welcome to this world"
print(s.startswith("welcome"))
#otherwise gives false

s = "welcome to THIS WORLD"
print(s.swapcase())
#converts lower case to upper, upper case to lower


s = "Welcome to this world"
print(s.title())
#convert string into title case, capitalize first characters of every word
