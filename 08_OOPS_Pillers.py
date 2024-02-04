# Python Abstraction
from abc import ABC, abstractmethod    # ABC (Abstract Base Class)

# Define an abstract class with abstract method(s)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Create a concrete class that inherits from the abstract class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implement the abstract methods
    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Create an instance of the concrete class
circle = Circle(radius=5)

# Call the methods on the instance
print("Area:", circle.area())  # Output: 78.5
print("Perimeter:", circle.perimeter())  # Output: 31.4





# Python Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog("Max")
dog.speak()




# Python Polymorphism 
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

class Student(Person):
    def greet(self):
        print("Hello, I'm a student named", self.name)

person1 = Person("Robert Downey")
student1 = Student("Junior")

person1.greet()
student1.greet()



# Python Encapsulation
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())

