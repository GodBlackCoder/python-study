#def is_not_empty(s):
#   return s and len(s.strip()) > 0
print filter(lambda x :  x and len(x.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])