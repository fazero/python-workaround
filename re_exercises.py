import re
p = re.compile('ab*')
p = re.compile(r'(?P<word>\b\w+\b)')
m = p.search( '(((( Lots of punctuation )))' )
print m.group('word')
print m.group(0)
print m.group(1)