class Animal:
	def __init__(self,name): # when object is called n this will auto happen
	
		self.name = name 
	
	def talk(self):
		pass
		
# going to reveal polymorphism		
class Dog(Animal):
	def talk(self):
		
		return "Woof"
		
class Cat(Animal):
	def talk(self):
		return "Meow"
		
#polymorphism meant change the parent formate

dog_goffy = Dog('Goffy')

print (dog_goffy.name)
print (dog_goffy.talk())

kitty = Cat("Kitty")
print (kitty.name)
print (kitty.talk())
