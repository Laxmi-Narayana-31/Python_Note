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

circle = Circle(radius=5)

print("Area:", circle.area())  # Output: 78.5
print("Perimeter:", circle.perimeter())  # Output: 31.4





# Python Inheritance (Single Inheritance)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}", "Woof!")

animal = Animal("Pet")
animal.speak()

dog = Dog("Max")
dog.speak()



# Multilevel Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says something")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

class GermanShepherd(Dog):
    def guard(self):
        print(f"{self.name} is guarding")

my_dog = GermanShepherd("Rex")

my_dog.speak()   # Calls speak method from Animal class
my_dog.bark()    # Calls bark method from Dog class
my_dog.guard()   # Calls guard method from GermanShepherd class





# Multiple inheritance
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bus(Vehicle):
    def transport_passengers(self):
        print("Bus is transporting passengers")

class CarAndBus(Car, Bus):
    def honk(self):
        print("Honk honk!")

vehicle_instance = CarAndBus("Toyota", "Camry")


vehicle_instance.display_info()            # Calls display_info method from Vehicle class
vehicle_instance.drive()                   # Calls drive method from Car class
vehicle_instance.transport_passengers()    # Calls transport_passengers method from Bus class
vehicle_instance.honk()                    # Calls honk method from CarAndBus class






# Hierarchical Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says something")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} meows")


my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")


my_dog.speak()   # Calls speak method from Animal class
my_dog.bark()    # Calls bark method from Dog class

my_cat.speak()   # Calls speak method from Animal class
my_cat.meow()    # Calls meow method from Cat class




# Hybrid Inheritance
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Motorcycle(Vehicle):
    def ride(self):
        print("Motorcycle is riding")

class HybridVehicle(Car, Motorcycle):
    def honk(self):
        print("Honk honk!")

hybrid_vehicle_instance = HybridVehicle("Toyota", "Prius")


hybrid_vehicle_instance.display_info()   # Calls display_info method from Vehicle class
hybrid_vehicle_instance.drive()          # Calls drive method from Car class
hybrid_vehicle_instance.ride()           # Calls ride method from Motorcycle class
hybrid_vehicle_instance.honk()           # Calls honk method from HybridVehicle class





# Python Polymorphism 
class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

car = Car()
boat = Boat()

car.move()
boat.move()




# Python Encapsulation
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self._model = model  # Protected attribute

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make


    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

my_car = Car("Toyota", "Camry")

print("Make:", my_car.get_make())
print("Model:", my_car.get_model())

my_car.set_make("Honda")
my_car.set_model("Accord")

print("Updated Make:", my_car.get_make())
print("Updated Model:", my_car.get_model())


