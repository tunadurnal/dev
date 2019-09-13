def findAlt(s, sub, end=None, r=False):
	out = []
	for i in range(len(s)-len(sub)+1):
		if s[i:i+len(sub)] == sub: out.append(i)
	if r: out = out[::-1]
	return out[:end] if out else -1

def splitAlt(s, sep=None, maxsplit=-1):
	if sep is None: flag = True; sep = ' '
	else: flag = False
	loc = findAlt(s, sep)
	if loc == -1: return [s]
	if maxsplit == -1: maxsplit = len(loc)
	res = [s[0:loc[0]]]
	for i in range(maxsplit):
		res.append(s[loc[i]+len(sep): None if i+1 == maxsplit else loc[i+1]])
	res = res if res[-1] else res[:-1]
	return [x for x in res if x] if flag else res

# print(splitAlt('    sensiz     olmaz    ki   ...     '))
# print(splitAlt('aga naber beya'))

def replaceAlt(s, old, new, count=None):
	count = count if count else len(s); x = 0
	for i in range(len(s)-len(old)+1):
		if s[i+x: i+len(old)+x] == old and count:
			s = s[:i+x] + new + s[i+len(old)+x:]
			count -= 1; x += len(new)-len(old)
	return s
# print(replaceAlt('adananan', 'an', 'fak', 2))

def stripAlt(s, chars=' '):
	for _ in range(2):
		for i in s:
			if i in chars: s = s.replace(i, '', 1)
			else: break
		s = s[::-1]
	return s
# print(repr(stripAlt('www.example.com', 'cmowz.')))

def titleAlt(s):
	for i in [s.find(x) for x in s.split()]:
		s = s[:i] + s[i].upper() + s[i+1:]
	return s
	
# print(repr(titleAlt('     sensiz    olmaz  ')))

def zfillAlt(s, w):
	return '-' + (w-len(s))*'0' + s[1:] if s[0] == '-' else (w-len(s))*'0'+s 

def bubblesort(l, key=None, r=False):
    if key is None: key = lambda x: x 
    i = len(l) - 1 
    while i > 0:
       	j = 0 
        while j < i: 
            if key(l[j]) > key(l[j+1]): l[j], l[j+1] = l[j+1], l[j] 
            j += 1 
        i -= 1 
    return l[::-1] if r else l

# print(bubblesort("This is a test string from Andrew".split(), key=str.lower))

def flatten(x):
	return flatten(x[0]) + (flatten(x[1:]) if len(x) > 1 else []) if isinstance(x, (list, tuple))  else [x]
# print(flatten([1,2,(3,4,(5,6,(7,8,(9,10))))]))

