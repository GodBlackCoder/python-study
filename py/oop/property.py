class Student(object):
	@property
	def score(self):
	    return self._score
	@score.setter
	def score(self, value):
		if not isinstance(value,int ):
			raise ValueError('score must be int ')
		if value < 0 or value > 100 :
			raise ValueError('score must between 1~100')
		self._score = value
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self, value):
		self._birth = value
	@property
	def age(self):
		return 2016 - self._birth	
student = Student();
student.score = 60
student.birth = 1992
student.score = 1000
print student.birth
print student.age
print student.score
	