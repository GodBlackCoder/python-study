class Person(object):
	def __init__(self,name,age,gender,score,**kw):
			self.name = name
			self.age = age
			self.gender = gender
			self.__score = score
			for key,value in kw.iteritems():
				self.key = value
				#print key
				setattr(self,key,value)
jack = Person('jack',20,'Man',60,job='coders',skill="java")
print jack.name,jack.job
print jack.skill
print jack.__score

