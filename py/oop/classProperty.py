class Person(object):
	count = 0 
	__counts = 0
	def __init__(self,name,age):
			self.name = name
			self.age = age
			Person.count = Person.count + 1
			Person.__counts = Person.__counts + 1			
jack = Person('jack',20)
jack.__counts = 5
print jack.count
print jack.__counts
tom  = Person('tom',19)
lin  = Person('lin',18)
print Person.count
print Person.__counts
 