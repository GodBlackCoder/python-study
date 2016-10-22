import time
import functools
def performance(type):
	def performance_decorator(f):
		@functools.wraps(f)
		def fn(*args, **kw):
			t1 = time.time()
			r = f(*args, **kw)
			t2 = time.time()
			if type == 'ms':
				t2=t2*60
			print 'call %s() in %f%s' % (f.__name__, (t2 - t1),type)
			return r
		return fn
	return performance_decorator

@performance('s')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
 
print factorial.__name__
print functools.partial