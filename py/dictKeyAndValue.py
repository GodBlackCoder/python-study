D={"tom":100,"jack":200,'Bob':300}
sum = 0.0
for key,value in D.items():
	print key,':',value
	sum = sum +value
print sum/len(D)
