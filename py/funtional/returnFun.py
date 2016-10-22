
def returnFun(lst):
	def fun():
		def multiple(x,y):
			return x*y
		return reduce(multiple,lst)
	return fun
f = returnFun([1,2,3])
print f()

