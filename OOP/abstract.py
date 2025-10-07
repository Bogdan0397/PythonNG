from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# animal = Animal()  # This will raise an error

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Bark
print(cat.speak())  # Output: Meow