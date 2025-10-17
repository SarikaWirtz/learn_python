#  Introducing the string data type
myString = "This is a string."
print(myString)
print(type(myString))
print(str(myString) + " is of the data type " + str(type(myString)))

# Working with string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString

print(thirdString)

# Working with input strings

name = input("What is your name?")
print(name)

# Formatting output strings

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
# number = input("give me any number?   ")

print("{}, you like a {} {}!".format(name,color,animal))

# print("{}, you like a {} {} {}!".format(name,color,animal, number))