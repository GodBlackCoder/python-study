class Fib(object):
 	def __init__(self, bound):
 		self.bound = bound
 		self.a,self.b = 0,1
 	def __iter__(self):
 		return self
 	def next(self):
 		self.a,self.b = self.b , self.a + self.b
 		if self.a > self.bound :
 			raise StopIteration()
 		return self.a
for n in Fib(100):
	print n
		