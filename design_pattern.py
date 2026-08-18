"""
Design Pattern
"""
# Singleton Pattern
class Singleton:
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance
# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)

#Factory Pattern

from abc import ABC, abstractmethod


class Animal(ABC):
	@abstractmethod
	def speak(self):
		pass


class Dog(Animal):
	def speak(self):
		return "Woof!"


class Cat(Animal):
	def speak(self):
		return "Meow!"


class AnimalFactory:
	def create_animal(self, animal_type):
		if animal_type == "dog":
			return Dog()
		elif animal_type == "cat":
			return Cat()
		else:
			raise ValueError("Unknown animal type")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
print(dog.speak()) 
print(cat.speak()) 

# Observer pattern

class Subject:
	def __init__(self):
		self._observers = []

	def attach(self, observer):
		self._observers.append(observer)

	def detach(self, observer):
		self._observers.remove(observer)

	def notify(self, message):
		for observer in self._observers:
			observer.update(message)


class Observer:
	def update(self, message):
		print(f"Received message: {message}")

# Usage
subject = Subject()
observer1 = Observer()
observer2 = Observer()
subject.attach(observer1)
subject.attach(observer2)
subject.notify("Hello Observers!")

# Strategy Pattern

class Context:
	def __init__(self, strategy):
		self._strategy = strategy

	def execute_strategy(self):
		return self._strategy.execute()


class Strategy:
	def execute(self):
		raise NotImplementedError("Subclass must implement execute method")


class ConcreteStrategyA(Strategy):
	def execute(self):
		return "Strategy A is executed"


class ConcreteStrategyB(Strategy):
	def execute(self):
		return "Strategy B is executed"

# Usage
context = Context(ConcreteStrategyA())
print(context.execute_strategy()) 
context = Context(ConcreteStrategyB())
print(context.execute_strategy()) 

"""
--> Output
True
Woof!
Meow!
Received message: Hello Observers!
Received message: Hello Observers!
Strategy A is executed
Strategy B is executed
"""