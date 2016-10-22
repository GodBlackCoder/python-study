def avg(*args):
	sum =0
	i=0
	if len(args) == 0:
		return 0 
	for var in args:
		sum = sum +var
		i=i+1
	return sum / i
print avg(1,2,3.8)
print avg()
