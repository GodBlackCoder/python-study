D={"tom":100,"jack":200,'Bob':300}
sum=0.0
for item in D.itervalues():
	sum = sum +item
avg= sum/len(D)
print 'avg score is %s' %avg