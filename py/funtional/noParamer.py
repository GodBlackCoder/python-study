def performence(f):
	def fn(*args,**kw):
		print 'funtion do',f.__name__,'()...'
		return f(*args,**kw)
	return fn
def firstUpper(string):
	#string2 = string.upper()
	return string[:1].upper() +string[1:].lower()
firstUpper=performence(firstUpper)
print map(firstUpper,['bart', 'LIsA', 'adam'])