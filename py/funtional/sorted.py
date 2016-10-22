def compare(x,y):
	if x[0].upper() >y[0].upper():
		return 1
	else :
		return -1
print sorted(['bob', 'about', 'Zoo', 'Credit'],compare)

