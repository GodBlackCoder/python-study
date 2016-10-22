import math
def is_sqrt(number):
	n = int(math.sqrt(number))
	return  n * n == number
print filter(is_sqrt,range(1,101))