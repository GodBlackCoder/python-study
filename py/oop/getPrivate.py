class Person(object):
	def __init__(self,name,age,score):
			self.name = name
			self.age = age
			self.__score = score
	def get_score(self):
		return self.__score
	def get_grade(self):
		if self.__score >70 :
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
jack = Person('jack',20,80)
tom  = Person('tom',19,60)
lin  = Person('lin',18,55)
print jack.get_score(),jack.get_grade()
print tom.get_score(),tom.get_grade()
print lin.get_score(),lin.get_grade()

 