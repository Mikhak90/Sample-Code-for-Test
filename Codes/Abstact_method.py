from abc import ABC


class Animal(ABC):
	def move(self):
		pass

class Monkey(Animal):
	def move(self):
		print("I can walk and jump")

class Bird(Animal):
	def move(self):
		print("I can fly")

class Snake(Animal):
	def move(self):
		print("I can crawl")

class Dog(Animal):
	def move(self):
		print("I can bark")

class Lion(Animal):
	def move(self):
		print("I can roar")


# Driver code
R = Bird()
R.move()

R=Monkey()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
