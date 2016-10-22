import functools
#sortedNoCase = functools.partial(sorted,cmp=lambda x,y:cmp(x.upper(),y.upper()))
#sortedNoCase = functools.partial(sorted,cmp=lambda x,y:cmp(x.upper(),y.upper()))
sortedNoCase =functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
#print sorted(['bob', 'about', 'Zoo', 'Credit'])
print sortedNoCase(['bob', 'about', 'Zoo', 'Credit'])