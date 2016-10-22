D={"tom":100,"jack":20,'Bob':300}
def fun(name,score):
	if score < 60 :
		return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
	return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
for tr in [fun(name,score) for name,score in D.items()] :
	print tr
tbs=[fun(name,score) for name,score in D.items()]
print '\n'.join([fun(name,score) for name,score in D.items()])
print '\n'.join(tbs)