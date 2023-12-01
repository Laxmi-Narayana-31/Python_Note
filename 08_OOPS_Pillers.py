# Python Abstraction
class Computer:
    def __init__(self):
        self.cpu = "Intel Core i5"
        self.memory = "16GB"
        self.storage = "512GB SSD"

    def turn_on(self):
        print("Computer is turning on...")
        # Perform internal hardware initialization

    def turn_off(self):
        print("Computer is turning off...")
        # Perform internal hardware shutdown

    def run_program(self, program):
        print("Executing program:", program)
        # Perform program execution using internal hardware

computer = Computer()
computer.turn_on()
computer.run_program("Web browser")
computer.turn_off()




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

