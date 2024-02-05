# Function is block of code that is used to perform some operations.
# In python, a function defined as "def" keyword


def my_function():
  print("Hello my name is SHIVA")

my_function()


# Argument: The values that are passed during function call
# Parameters: Variables in the function definition which accepts arguments
# Arguments are often shortened to args in Python


def my_info(name,age,city,country): # -> Parameters 
   print(f"My name is {name} and my age is {age}. I am from {city},{country}")

   print("My name is {} and my age is {}. I am from {},{}".format(name, age, city, country))

my_info("SHIVA",23,"BBSR","INDIA") # -> Arguments


# Return statement : It returns value back to where it was called
def add_numbers(a,b):
    return a+b
result = add_numbers(10,5)
print(result)



# Arbitary Arguments -> Shortly referrred as *args
"""If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:"""


def my_function(*name):
  print("My name was -> " + name[1])

my_function("shiva", "sumit", "amit")


# Keyword Arguments -> you can send arguments in key = value pair
def my_function2(name1,name2,name3):
    print("Name was -> ",name3)
my_function2(name1="sumit",name2="sonu",name3='shiva')



# Arbitrary Keyword Arguments -> **kwargs
'''If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition. If the number of keyword arguments is unknown, add a double ** before the parameter name:'''
def my_function(**name):
  print("My last name is " + name["lname"])

my_function(fname = "Laxmi", lname = "Narayana")



def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Passing a list in a function
def my_function(name_list):
    for name in name_list:
        print(name)

list_of_names = ['shiva','amit','sonu','sumit']
my_function(list_of_names)


# When you declare a function,it must have a definition. If some reason have function definition with no content ,simply write pass statement to avoid error

def demo_function():
    pass


# Recursion : Whenever a function calls itself repeatedily until a certain condition reachedd called recursion.


# Lambda : A lambda function is a small anonymous function that takes any number of arguments, but can only have a one expression

x = lambda a: a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# Why use -> when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(24))    # output: 48
