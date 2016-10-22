class Student(object):
 	def __init__(self, name):
 		self.name = name
	def __str__(self):
		return 'Student:%s'% self.name
	__repr__ = __str__
student = Student('tom')
print student
student

		