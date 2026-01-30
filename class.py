class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
    

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):  # Concrete subclass
    def make_sound(self):
        return "Bark!"
    
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.fuel_level = 100  # Initial fuel level


class Car:
    # ... (attributes)

    def start_engine(self):
        print(f"The {self.year} {self.make} {self.model}'s engine roars to life!")

    def accelerate(self):
        print(f"The {self.color} {self.make} {self.model} picks up speed!")

    def brake(self):
        print(f"The {self.make} {self.model} comes to a smooth stop.")

# Add your class definition here (steps 1-3)
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed


    def bark(self):
        print('Woof!My name is ',self.name,' and I\'m a',self.breed)
    

# Creating the instance of the Dog class (step 4)
my_dog = Dog("Buddy", "Golden Retriever")
# Directing the dog to bark (step 5)
my_dog.bark()