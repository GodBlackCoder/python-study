class Person(object):
	__count = 0
	@classmethod
	def getCount(cls):
		return cls.__count
	def __init__(self, name, score):
		self.name = name
		self.score = score
		self.get_grade = lambda: 'A'
		Person.__count = Person.__count +1
p1 = Person('Bob', 90)
print p1.getCount()
p2 = Person('Bob', 90)
print Person.getCount()