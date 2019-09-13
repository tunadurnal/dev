import itertools, operator, collections
class groupby:
    def __init__(self, iterable, key=None):
        if key is None: key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def __next__(self):
        while self.tgtkey == self.currkey:
            self.currvalue = next(self.it)
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper())
    def _grouper(self):
        while self.tgtkey == self.currkey:
            yield self.currvalue
            try: self.currvalue = next(self.it)
            except StopIteration: return
            self.currkey = self.keyfunc(self.currvalue)
print([(k, list(g)) for k, g in groupby('AAABBBABBCCCDDDBDDA')])

def myslice(iterable, *args):
    return iterable[slice(args[0], args[0]+1)] if len(args) < 2 else iterable[slice(*args)]
print(myslice('tunadurnal', 5))
def cycle(p):
    # cycle('ABCD') --> A B C D A B C D ...
    saved = []
    for elem in p: yield elem; saved.append(elem)
    while saved:
        for elem in saved: yield elem
def count(start, step=1):
    # count(1, 2) --> 1, 3, 5, 7, 9 ...
    # count(3.0, 0.5) --> 3.0, 3.5, 4.0 ...
    while 1:
        yield start
        start += step
def repeat(obj, times=None):
    if times is None:
        while 1: yield obj
    else:
        for i in range(times): yield obj
def accumulate(iterable, func=operator.add):
    # accumulate([1,2,3,4,5]) --> 1, 3, 6, 10, 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1, 2, 6, 24, 120
    it = iter(iterable)
    try: total = next(it)
    except StopIteration: return
    yield total
    for elem in it:
        total = func(total, elem)
        yield total
def reduce(func, iterable, initializer=None):
    it = iter(iterable)
    value = next(it) if initializer is None else initializer
    for elem in it: value = func(value, elem)
    return value
def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                try:
                    newval = next(it)   # fetch a new value and
                except StopIteration:
                    return
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)
print(tee('tuna'))
def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x): yield x; break
    for x in iterable: yield x
def takewhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if predicate(x): yield x
        else: break
print(tuple(takewhile(lambda x: x<5, [1,4,6,4,1])))
def mapAlt(func, iterable):
    it = iter(iterable)
    for elem in it: yield func(elem)
def compress(data, selectors):
    return (d for d, s in zip(data, selectors) if s)
def filterAlt(predicate, iterable):
    if predicate is None: predicate = bool
    iterator = iter(iterable)
    for elem in iterator:
        if predicate(elem): yield elem
def filterfalse(predicate, iterable):
    if predicate is None: predicate = bool
    iterator = iter(iterable)
    for elem in iterator:
        if not predicate(elem): yield elem
def izip(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            try: elem = next(it)
            except StopIteration: return
            else: result.append(elem)
        yield tuple(result)

def chain(*iterables):
    for it in iterables:
        for elem in it: yield elem
def g2():
    for i in range(10): yield i
def g3():
    for i in range(10, 20): yield i

def g():
    yield from g2(); yield from g3()
def altG():
    for i in itertools.chain(g2(), g3()): yield i
print(list(g()), list(altG()))

