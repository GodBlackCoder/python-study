class Animal(object):
	def call(self):
		print 'i am a animal'
class Runnable(object):
	def run(self):
		print 'runing....'
class Dog(Animal,Runnable):
	def pro(self):
		super(Dog,self).call()
		super(Dog,self).run()
dogTom =  Dog()
dogTom.pro()
		