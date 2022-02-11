a = "Hello World!"
A = ["Sol Goodguy","Bruh","Penis","M1 Max Pro lol"]
print(a)
print(A[0],A[1])
b = [A[0]] + [A[1]] + [[1,2,3,4,5]]
print(A)
"""
A variable is used to store data that will be used by the program. 

This data can be a number, a string, a Boolean, a list or some other data type. 

Every variable has a name which can consist of letters, numbers, and the underscore character _.

The equal sign = is used to assign a value to a variable.

After the initial assignment is made, the value of a variable can be updated to new values as needed.
"""
# These are all valid variable names and assignment
 
user_name = "@StormHAWK814"
user_id = 100
verified = False
 
# A variable's value can be changed after assignment
 
points = 100
points = 120

# This is a comment 

# Bottom Text

"""
This is a multiline comment.
Print prints shit
Curley brackets passes arguments to functions. 
Example: Print is the fucntuion and everything inside is the argument.
0 Always comes first then 1. It goes in a list.
Example: 0,1,2,3,4,5
I can use equal to assign value to a variable. 
For example a word.
[]: Used to define mutable data types - lists, list comprehensions and for indexing/lookup/slicing.
(): Define tuples, order of operations, generator expressions, function calls and other syntax.
{}: The two hash table types - dictionaries and sets.
Straight bracket makes the athormentioned list of items. 
To seperate shit you use a comma. "Hello","World" 
+ adds shit on top. 
Example: B all ready means shit. 
So if I add + and straight brackets for a list I can add numbers or other data.
I can also shift it around. 
2 Quotation marks makes an empty string. This allows you to
"""
"""
"Your Mother"  is a string that contains the text "your mother"
"" is also a string, it contains the text "", so nothing. basically it's a blank string, but it's still a string.
the .join part is complicated, it gets into Python's object-oriented side and :bruh:
"""

"".join([x for x in "" if x in "hkmcrnae"])
if 5 > 2:
  print("Five hugs is greater than two!")
  
  
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "Adam"
print(x)
print(y)
x = 4 # x is of type int
x = "Adam" # x is now of type str
print(x)
# Variables do not need to be declared with any particular type, and can even change type after they have been set.

# String variables can be declared either by using single or double quotes: 
x = "Adam"
# is the same as
x = 'Adam'

#This is an associative array/Dictornary
c = {"favcolour":"Black" }
print(c)

"""
Set is a list except it doesn't have order nor repetition. 
To start it off use two curley brackets but don't use the colon when making a set. 
"""
d = {1,2,3,4,5,6,7,8,9,9,9,9,9,9,9}
print(d)

if 1 == 1: 
  print ("Duh")
  
if 1==2: 
  print("Abit studpid ennit")
  
#booleans 

True

False

True or False 

True and False 

for int in range(0,8): 
  print (int)
# A for loop in Python is a control flow statement. 
# It's used to repeatedly execute a group of statements as long as the condition is satisfied.

for item in b:
  print(item)

k = 7 
while k > 5:
  print(k)
  k -= 1 #The -= 1 prevents an infinite loop.

try:
  print(A[2])
except IndexError:
  print("Item does not exist") #It litteraly doesn't exist 

def SolBadguy():
  print("Hello World!")

SolBadguy()

class person:
  def __init__(self):
    print("New Person")

p = person()

class Francis(person):
  def __init__(self):
    print("My name is Francis!")

  def SolBadguy():
    print("Ky Kiske")

francis_object = Francis()
francis_object.SolBadguy()

"""
Different Maths operations.
+ for addition
- for subtraction
* for multiplication
/ for division
% for modulus returns the remainder
** for exponentiation
"""
 
result = 10 + 30
result = 40 - 10
result = 50 * 5
result = 16 / 4
result = 25 % 2
result = 5 ** 3
"""
The plus-equals operator += provides a convenient way to add a value to an existing variable and assign the new value back to the same variable.

In the case where the variable and the value are strings, this operator performs string concatention instead of addition.

The operation is performed in-place, meaning that any other variable which points to the variable being updated will also be updated.
"""

# Plus-Equal Operator
 
counter = 0
counter += 10
 
# This is equivalent to
 
counter = 0
counter = counter + 10
 
# The operator will also perform string concatenation
 
message = "Part 1 of message "
message += "Part 2 of message"
print(message)

"""
A string is a sequence of characters (letters, numbers, whitespace or punctuation) enclosed by quotation marks.

It can be enclosed using either the double quotation mark " or the single quotation mark '.

If a string has to be broken into multiple lines, the backslash character \ can be used to indicate that the string continues on the next line.
"""

user = "STORM"
game = 'GGST'
 
longer = "This string is broken up \
over multiple lines"

"""
A SyntaxError is reported by the Python interpreter when some portion of the code is incorrect. 

This can include misspelled: 

keywords, missing or too many brackets or parenthesis, incorrect operators, missing or too many quotation marks, or other conditions.
"""

"""
A NameError is reported by the Python interpreter when it detects a variable that is unknown. 

This can occur when a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined. 

The Python interpreter will display the line of code where the NameError was detected and indicate which name it found that was not defined.
"""

"""
Floating Point Numbers

Python variables can be assigned different types of data. 

One supported data type is the floating point number. 

A floating point number is a value that contains a decimal portion.

It can be used to represent numbers that have fractional quantities.

For example, a = 3/5 can not be represented as an integer, so the variable a is assigned a floating point value of 0.6.
"""
# Floating point numbers
 
pi = 3.14159
meal_cost = 12.99
tip_percent = 0.20 #Decimals basicly.

"""
The Python or operator combines two Boolean expressions and evaluates to True if at least one of the expressions returns True. 

Otherwise, if both expressions are False, then the entire expression evaluates to False.
"""
True or True      # Evaluates to True
True or False     # Evaluates to True
False or False    # Evaluates to False
1 < 2 or 3 < 1    # Evaluates to True
3 < 1 or 1 > 6    # Evaluates to False
1 == 1 or 1 < 2   # Evaluates to True

"""
The Python elif statement allows for continued checks to be performed after an initial if statement. 

An elif statement differs from the else statement because another expression is provided to be checked, just as with the initial if statement.

If the expression is True, the indented code following the elif is executed. 

If the expression evaluates to False, the code can continue to an optional else statement. 

Multiple elif statements can be used following an initial if to perform a series of checks. 

Once an elif expression evaluates to True, no further elif statements are executed.
"""
# elif Statement
 
item_type = "Gun"
 
if item_type == "pen":
  print("You have a pen.")
elif item_type == "pineapple":
  print("You have a Pineapple.")
elif item_type == "Pen":
  # this is performed
  print("You have a pen")
else:
  print("Not sure!")

"""
The equal operator, ==, is used to compare two values, variables or expressions to determine if they are the same.

If the values being compared are the same, the operator returns True, otherwise it returns False.

The operator takes the data type into account when making the comparison, so a string value of "2" is not considered the same as a numeric value of 2.
"""
# Equal operator
 
if 'Yes' == 'Yes':
  # evaluates to True
  print('They are equal')
 
if (2 > 1) == (5 < 10):
  # evaluates to True
  print('Both expressions give the same result')
 
c = '2'
d = 2
 
if c == d:
  print('They are equal')
else:
  print('They are not equal')

  