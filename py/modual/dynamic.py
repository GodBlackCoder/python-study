try:
	import json as json
except ImportError:
	import simplejson as json
	print 'import simplejsons'
else:
	print 'sucess'
finally:
	print  json.dumps({'python':2.7})
print 10 /3