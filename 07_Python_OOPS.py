'''Python is Object oriented Programming language.
OOPs concept - 
1. class : It is a collection of objects. It is a logical entity.

2. Object: An instance of the class, which has its own state and behavior.
Example, a parrot is an object. It has
attributes - name, age, color, etc.
behavior - dancing, singing, etc.

3. Polymorphism : Polymorphism simply means having many forms.
4. Inheritance : Inheritance is the capability of one class to derive or inherit the properties from another class.
5. Encapsulation : It describes the idea of wrapping data and the methods that work on data within one unit.
6. Abstraction : It hides unnecessary code details from the user.'''

# class Demo: # class name is Demo
#     a = 5
# myobj = Demo() # myobj -> Name of the object 
# print(myobj.a)

'''class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.'''

class Person:
  pass


# __init__() function -> It is kind same like a Constructor
'''It is a built in functin in python. All classes have a function called __init__(), which is always executed when the class is being initiated.
__init__() function is called automatically every time the class is being used to create a new object.'''



# class Demo:
#     def __init__(self,name,age,city):
#         self.name = name
#         self.age = age
#         self.city = city
# # MyObj = Demo('shiva',25,'BBSR') # Objeccreation and pass the parameters
# # print(MyObj.name)
# # print(MyObj.age)
# # print(MyObj.city)




# __str__() function -> It controls what should be returned when the class object is represented as a string.

# string representation of an object WITHOUT the __str__() function
'''class Demo:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
person1 = Demo('Shiva', 23, 'BBSR')
print(person1) # Output : <__main__.Demo object at 0x0000015EE46A8350>'''


# String representation of an object with the __str__() function
'''class Demo:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f'{self.name} ({self.age}) ({self.city})'

person1 = Demo('Shiva', 23, 'BBSR')
print(person1)  # Output : Shiva (23) (BBSR)'''




'''class Demo:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def displayInfo(self): # displayInfo -> It is a method 
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

person1 = Demo('Shiva', 23, 'BBSR') # person1 -> object name 
person1.displayInfo()'''



'''The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class'''

'''class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(demo):
    print("Hello my name is " + demo.name + "and my age is " + str(demo.age)) # Typecasting -> str(demo.age)) can only concatenate str (not "int") to str

p1 = Person("Shiva", 22)
p1.myfunc()'''


class shiva:
    def __init__(self):
        self.name = "Shiva"
        self.age = 40
        self.color = "Black"

    # method to display information about the object
    def info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Color : ", self.color)

Myobj = shiva()
Myobj.info()

# modify the object 
Myobj.name = "Laxmi_Narayana"
print("\nAfter modification name was", Myobj.name)

# delete object properties 
del Myobj.age

# delte object
del Myobj

# print(Myobj.name) 
'''NameError: name 'Myobj' is not defined, because you delete the Myobj'''
            



# Python Inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Shiva", "Pattanayak")
x.printname() 

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.

# Inheriting all properties of Person class 
class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname) # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function

    super().__init__(fname, lname) # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
    




# Add a propert city to the student class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()



# Python polymorphism
'''Python function that can be used on different objects is the len() function.
1. For strings len() returns the number of characters.

x = "Hello World!"
print(len(x))

2. For tuples len() returns the number of items in the tuple.

mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

3. For dictionaries len() returns the number of key/value pairs in the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))'''


# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()