# It was created by Guido van Rossum, and released in 1991.
# Python is case sensetive language


# Comments are 2 types in python - use # symbol  or use triple quotes(either single quotes ''' or double quotes """)

# VS Code shortcut keys
"""  Shift + "" for triple quote comments

 Ctrl + Shift + L -> Multiline editing. Select the word you want to edit then press Ctrl + Shift + L

 Ctrl + Shift + H -> Replace all words with another word"""


"""
 if 5 > 2:  # if (5>2)
    print("Five is greater than two!")
    print("Five is greater than two!")  """


# Dynamically typed, there is no need to specify the data type
"""
x=4  
print (type(x))   #<class 'int'>

y='a'
print (type(y))   #<class 'str'>

a="Shiva"
print (type(a))   #<class 'str'>

b=1.5
print (type(b))   #<class 'float'>
"""


# Type casting -> Convert the one data type to another

"""x = str(10)    # x will be '10'
y = int(10)       # y will be 10
z = float(10)     # z will be 10.0


'''You can get the data type of a variable with the type() function.'''
print(x)
print(type(x))

print(y)
print(type(y))

print(z)
print(type(z))"""


"""print("hello")  
 
if 5>2:  # if(5>2)
  print("Five is greater than two!")


if 5 > 2:
  print("Five is greater than two!") 
 """


# Variable -> These are case sensetive
"""myvar = "Shiva"
my_var = "Shiva"
_my_var = "Shiva"
myVar = "Shiva"
MYVAR = "Shiva"
myvar2 = "Shiva"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)"""


# Variable Naming Convention
"""myVariableName = "Shiva"  # Camel case
MyVariableName = "Shiva"  # Pascal case 
my_variable_name = "Shiva" # Snake case"""


# Python allows you to assign values to multiple variables in one line
"""a,b,c = "shiva", 10 , 123.5
print(a,b,c)


a=b=c=10
print(a, b, c)  # 10 10 10


# a=b=c=10,45
# print(a, b, c)  # (10, 45) (10, 45) (10, 45)


a=b=c="Shiva", "Sumit", "Amit"
print(a,b,c)  # ('Shiva', 'Sumit', 'Amit') ('Shiva', 'Sumit', 'Amit') ('Shiva', 'Sumit', 'Amit') 


names = ["Shiva","Sumit","Amit", "Laxmi_Narayana"]
a,b,c,d= names
print(a,b,c,d)

print(a)
print(b)
print(c)
print(d)


a="Laxmi"
b="Narayana"
c="Pattanayak"
print(a,b,c)   # Laxmi Narayana Pattanayak
print(a + b + c)   # LaxmiNarayanaPattanayak


a="Python " # Give proper space for readbility
b="is "
c="older "
d="than "
e="Java"
print(a+b+c+d+e)"""


# In Pyhton, if you are Attempting to convert a non-numeric string like "Shiva" to an integer using int() will result in a ValueError

"""
string_value = "123"  # A string containing a numeric value
integer_value = int(string_value)  # Convert the string to an integer
print(integer_value)  # Output: 123"""

"""name = "shiva" 
newName = int(name)  -> This concersion gives a value error
print(newName)"""


# Variable is 2 types : Local and Global
"""Local : Declred with in function and scope is with in function.
Global : Not declred with in function (declared outside the function) , Scope is through out the program.

If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""

# x = "awesome"  # -> Global
# print(x)
# print("The address of this x is:",id(x)) 
 
# def myfunc():
#   global x
#   x = "fantastic" #-> Global because it declared with global keyword
#   print("The address of this x with in function is :",x,id(x))

# myfunc()

# print("Python is " + x)   # Python is fantastic, Here this x is global
# print(id(x))


"""x = "awesome" # -> Global 
print("The address of this x is :", id(x))

def myfunc():
  x = "fantastic"  # -> Local
  print("The address of this x with in function is:",id(x))
  print("Python is " + x)  # Python is fantastic

myfunc()

print("Python is " + x)  # Python is awesome
print("Address of x ,After function call",id(x)) #-> This x is global"""


# Data types

"""
Txt Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType  """

"""
string -> x = "Hello World"
integer -> x = 1024
float  -> x = 10.5
complex -> x= 1jk """

"""List -> ["Shiva", "Sumit", "Amit"]
Tuple -> (1, "Shiva", True)
Dictitonary -> {"Name" : "Shiva", "Age": "22", "City" : "Berhampur"}
Set -> {"Shiva", "Sonu", "Amit"}
Frozen Set -> {frozenset({"Shiva","Sonu"})}
Boolean -> x = True , x= False """


# Setting the Specific Data Type
"""x = str("Hello World")		
x = int(20)		
x = float(20.5)		
x = complex(1j)		
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)		
x = dict(name="Shiva", age=22)		
x = set(("apple", "banana", "cherry"))		
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)"""


# Return the data tyoe size in form of "Bytes" 1 Byte = 8 bits
#import sys
# print('size of integer :--> ', sys.getsizeof(int()))
# print('size of float:--> ', sys.getsizeof(float()))
# print('size of string :--> ', sys.getsizeof(str()))
# print('size of list :--> ', sys.getsizeof(list()))
# print('size of set :--> ', sys.getsizeof(set()))
# print('size of tuple :--> ', sys.getsizeof(tuple()))
# print('size of dictitonary :--> ', sys.getsizeof(dict()))


# Random Number
"""Python has a module called random. With help of this we make any random no  """

# import random
# random_number = random.randint(1, 100) # Generate Random Integer Between 1 to 100
# print(random_number)


# a = """Hey i am laxmi narayana pattanyak. Currently persuing my masters in computer application from GIET University"""
# print(a)



# String -> Enclosed with single or double quotes
"""a = "Hello, World!"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])"""


'''  
str = 'Hello World'
for x in str:  # Iterate using loop
  print(x)

print("The length of str is:",len(str)) # Returns string length


# Check particular word or character present in string or not
print("Hello" in str) # It returns Boolean value 


if("Hello " in str):
  print("Yes, Hello is present in the string.")
else:
  print("No, Hello isn't present in the string.")


print("War" not in str) # Return Boolean value '''


# Slicing -> It retuns the range of characters by using this 
'''
str1 = "Hello, World!"
print(len(str1))
print(str1[2:5]) # [2:5] index 2 included but index 5 is not included

print(str1[-1]) # it returns len(str1)-1= 13-1=12(returns 12 index position)  (-1 refers last element)

print(str1[:5]) # Nothing in strt position means it starts from index 0 position

print(str1[8:]) # From index 8 till end (not include 9th index)

print(str1[-5:-2]) # str1[len(str1)-5 : len(str1)-2] = 13-5 : 13-2 = 8:11  '''


# String Modification

"""str2 = "     Hello, World!  "
print(str2.upper())
print(str2.lower())
print(str2.replace('World', 'Python')) # World is replaced with Python
print(str2.strip()) # strip() removes all white spaces at beginning and end positions
print(str2.split('e'))"""


# Concatenation
str1 = "Laxmi"
"""str2 = "Narayana"
str2 = "Pattanayak"
name = str1 + str2 + str2
print(name)
print(str1 + str2 + str2) # LaxmiNarayanaPattanayak
print(str1+" "+str2+" "+str2) # Laxmi Narayana Pattanayak

age = 22
country = 'India'

txt= "My name is {} and my age is {}".format(name,age)
print(txt)

print("{} lives in {}".format(name , country ))


full_sentence = "My name is "+name+ "and my age is "+ str(age) # If you add just age it give  TypeError: can only concatenate str (not "int") to str
print(full_sentence )

txt2 = "I am Shiva \"Hello\" from India"
print(txt2)"""



 # STRING METHODS
"""str = "hello!"
print(str.capitalize())   # Converts the first character of this string to a capital letter

str1= "HELLO, WORLD!"
print(str1.casefold())    # Case folding converts all characters in this string into lower case letters

print(str.center(30))  # give 30 space before HELLO, WORLD!
print(str.center(30,'@'))  # @@@@@@@@@@@@hello!@@@@@@@@@@@@ The length is 30


str2 = "Laxmi Narayana Pattanayak"
print(str2.count('a'))  # count() method returns the number of times a specified value appears in the string. 
print(str2.count('a',6,24)) # Find the no of 'a' from index 6 to index 24"""
'''Count number of 'a' present in str2 '''



"""txt = "My name is Shiva"
x = txt.encode()
print(x)

y = x.decode()
print(type(y), y)


str3 = "Shiva Sumit Amit"
print(str3.endswith('t')) # Return Boolean value

# expandtabs()->Sets the tab size of the string
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(6)
print(x)  """

'''
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))'''


# find() method finds the first occurance of the specified value.
# find()method returns -1 if the value is not found.
# txt2 = "Hello, I am Laxmi Narayana Pattanayak. I currently persuing MCA from GIET"
# print(txt2.find("Laxmi"))
# print(txt2.find("I"))
# print(txt2[7])
# # Syntax - string.find(value, start, end)
# print(txt2.find('a',12,23))
# print(txt2.find('a'))


# # format() method
# txt3 = "For only {price:.2f} dollars"
# print(txt3.format(price=40))


# txt1 = "My name is {fname}, I'm {age}".format(fname = "Shiva", age = 22)
# txt2 = "My name is {0}, I'm {1}".format("Shiva",22)
# txt3 = "My name is {}, I'm {}".format("Shiva",22)

# print(txt1)
# print(txt2)
# print(txt3)



# format_map()
"""name = "Laxmi Narayana Pattanayak"
data = {"name": name}
x = "My name is {name}".format_map(data)
print(x)"""


# y= name.index("Nar")
# print(y)

# z= name.index('a',12,23)
# print(z)
# find() and index() method both are used to find the first occurance of substring with in a string. 
# The only difference is :
# in index() method -> if the substring is not found, it raises ValueError while find() method returns '-1' indicate the sunstring is not found in the string




# isalnum() -> it checks all the characters in the text are alphanumeric or not. It rerurn a boolean vlue
"""txt="abcde567890"
print(txt.isalnum()) -> True """


# isalpha()-> checks all the characters in string are alphabet or not 
"""txt1 = "shiva"
txt2 = "shiva123"
print(txt1.isalpha()) -> True 
print(txt2.isalpha()) -> False """



# istitle() -> Check if each word start with an upper case letter

"""txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)




# join() -> join tuple items into a string using a hash character as separator
myTuple =['shiva','amit','sonu','sumit']
str ='@'.join(myTuple)  #-> shiva@amit@sonu@sumit
print(str)"""



"""fruit = "     apple    "
x = fruit.ljust(10)  #-> No of spces in parentesis
print(x,"is good for health")

y = fruit.lstrip()  #lstrip() -> Remove spaces to the left of the string
print("Benefit of",y,"-> It is good for health")"""



# partition() method search for a particular string, and split the string into a tuple containg three elements.
# lower(),capitalize(),title() -> Converts All Letters In String To Lowercase / Capital Case / Title Case


"""name ="Hey, I am Laxmi Narayana Pattanayak"
print(name.partition('Laxmi'))
 
sentence = "India is a beautiful country with lot of diversity in different areas"
print(sentence.partition('country')) # if the specified string is not found it will put whole sentence in a sinle part and two empty part '', ''"""



# replace() -> Replace a specified value with another specified value
"""name = 'Laxmi Narayana Pattanayak'
print(name.replace('Laxmi Narayana','Shiva'))

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 1)
print(x)"""


# rfind() -> Find last occurance of a element
# It returns -1 if the value is not found. It is same as rindex() method
"""txt="I love Python Programming Language"
txt1="I love Python Programming Language, Python"
print(txt.rfind('Python'))
print(txt1.rfind('Python'))
print(txt.rindex('Python'))"""

# split() -> Split the string into the list
"""txt="I love Python Programming Language"
print(txt.split())

txt2 = 'I love\n Python\n Programming\n Language'
print(txt2.splitlines())"""

# strip()-> remove all white spaces at beginning and ending of the string. You can also specify the which charcter you want to remove.

"""txt3='   Hello World!      '
print(txt3.strip())


txt4=",,,,,rrttgg.....banana....rrr"
x= txt4.strip(',.rtg')
print(x)"""


# swapcase -> Make the lower case letters to upper case and vice-versa.
# name = "Hey I am Laxmi Narayana Pattanayak"
# print (name.swapcase())

# title -> Make the first letter in each word upper case
"""txt = "hey i am good"
print(txt.title())
"""

'''
 txt = "50"
x = txt.zfill(4)
print(x)'''


# Python Booleans  -> True or False
'''print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))
print(bool(15))


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))'''




#Operator Precedence
"""
()	 ----->  Parentheses	
**	 ----->  Exponentiation	
+x  -x  ~x	-----> Unary plus, unary minus, and bitwise NOT	
*  /  //  %  ---->  Multiplication, division, floor division, and modulus	
+  -	  ----->   Addition and subtraction	
<<  >>	---->     Bitwise left and right shifts	
&	 ----->   Bitwise AND	
^	 ----->   Bitwise XOR	
|	 ----->   Bitwise OR	
==  !=  >  >=  <  <=   -----> Comparisons operators	
is  is not -----> Identity operator 
in  not in -----> Membership operators
not	----->  Logical NOT	
and	----->  Logical AND	
or  -----> 	Logical OR"""


