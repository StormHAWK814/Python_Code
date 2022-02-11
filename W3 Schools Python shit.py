from typing import Text


x = 4 #x is now a type of interger 
X = "Adam" # x is now a string 
print(x)
print(X)

y = str(3) # This will be '3'
w = int(3) # This will be just 3
z = float(3)# This will be 3 with a decimal place

h = 5 
k = "Adam"
print(type(h))
print(type(k))

n = "Adam"
N = 'Adam'
print(n)
print()
print(N)
# "Is a string." 'This is also a string.' You can use either or.

myvar = "Adam"
my_var = "Adam"
_my_var = "Adam"
myVar = "Adam"
MYVAR = "Adam"
myvar2 = "Adam"
_my_Var2 = "Adam"
_My_Var2 = "Adam"

myVariableName = "Adam" # Cammel Case. Each word, except the first, starts with a capital letter.
MyVariableName = "Adam" # Pascal Case. Each word starts with a capital letter.
my_variable_name = "Adam" # Snake Case. Each word is separated by an underscore character.

d,y,z = "Orange", "Red", "Green"
print(d,y,z) # You can turn it in to a list.

c = "Pog"
print("Python is " + c) # To combine both text and a variable, Python uses the + character. It also works as a mathmatical orperator.

Ex = 5 
Br = 10
print(Ex + Br)

def myfunc():
    print("Python is " + c)
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.
myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

c = "Pog"

def myfunc():
    c = "poggers"
    print("Python is " + c) 

myfunc()
    
print("Python is " + c)

def myfunc():
    global c 
    c = "poggers"

""" 
In programming data type is an important concept. 

Since valuables can store data of different types and different types can do different things.

Python has the following data types built in by default in these categories. 
""" 

# Text Type 

str() #The str() function converts the specified value into a string.

# Numeric types

int() # The int() function converts the specified value into an integer number. 

float() # Converts a number stored in a string or integer into a floating point number, or a number with a decimal point.

complex() # It is used to convert numbers or string into a complex number.

# Sequence Types 

list() # The list() function converts the specified value.

tuple # It's a data structure that store an ordered sequence of values.

