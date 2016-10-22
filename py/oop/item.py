class Fib(object):
	def __init__(this):
		this.name ='Fib'
	def __getattr__(this,attr):
		if attr == 'info':
			return 'i am Fib'
	def __getitem__(self,n):
		if isinstance(n,int):
			a , b = 1 , 1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			a , b = 1 , 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L
f = Fib()
print f[5]
print f[0:5]
print f[1:10]
print f.name
print f.info




		