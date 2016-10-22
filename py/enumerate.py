L = ['Bob','Jack','Lucy']
#for index,name in  enumerate(L) :
#	print index ,'-' ,name
for item in zip(L,range(1,4)) :
	print '%-4s - %s' %(item[0],item[1])

