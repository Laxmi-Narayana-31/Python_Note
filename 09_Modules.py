# Module -> A file containing a set of functions you want to include in your application.

'''person1 = {      # Save it as MyInfo.py
"name":"Shiva",
"age":23,
"city":"BBSR",
"country":"India"
}

import MyInfo
a = MyInfo.person1['age']
print(a)'''

# import platform
# x = platform.system()
# print(x)


# import platform
# x = dir(platform)
# print(x)


# Python Dates -> A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.



# import datetime
# x = datetime.datetime.now()
# print("Current date and time: ", x)
# print(x.year)
# print(x.strftime("%A"))
# print(x.strftime("%B"))

# y = datetime.datetime(2023,11,19) # YY/MM/DD
# print(y)



x = min(5, 10, 25) 
y = max(5, 10, 25)

print("The minimum elements is :",x)
print("The maximum elements is :",y)


z = abs(-9.45)
print("Absolute value is :", z)


# Power of a number
power = pow(5,3)
print("Power of 5 is :", power)


# Square root of a number
import math
sqrt_num = math.sqrt(64)
print(sqrt_num)

a = math.ceil(1.4)
b = math.floor(3.5)
print(a)
print(b)

pi_value = math.pi
print(pi_value)



# JSON -> It is for storing and exchanging data. JSON is a text, written with JavaScript object notation.
import json
data = {"Name":"Shiva", "Age": 23, "City": "Berhampur"}
json_object = json.dumps(data)
print(type(json_object))

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)




import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



'''When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent - 

dict   -> Object
list	-> Array
tuple   ->	Array
str	  -> String
int	 -> Number
float  -> 	Number
True  -> true
False	-> false
None	-> null'''



import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))