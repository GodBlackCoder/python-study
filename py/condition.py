def toUpper(L):
	return [x.upper() for x in L if isinstance(x,str)]
print toUpper(['tom',100,'jack'])