import collections
import logging
from logging import debug
logging.basicConfig(level=logging.DEBUG)

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(-5, 6)
print(p, p[0])

# ^ iki yönlü küme farkı
'''
>>> A = collections.Counter([1, 2, 2])
>>> B = collections.Counter([2, 2, 3])
>>> A
Counter({2: 2, 1: 1})
>>> B
Counter({2: 2, 3: 1})
>>> A | B
Counter({2: 2, 1: 1, 3: 1})
>>> A & B
Counter({2: 2})
>>> A + B
Counter({2: 4, 1: 1, 3: 1})
>>> A - B
Counter({1: 1})
>>> B - A
Counter({3: 1})

>>> A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
>>> A
Counter({3: 4, 1: 2, 2: 2, 4: 1, 5: 1, 6: 1, 7: 1})
>>> A.most_common(1)
[(3, 4)]
>>> A.most_common(3)
[(3, 4), (1, 2), (2, 2)]

>>> Q = collections.deque()
>>> Q.append(1)
>>> Q.appendleft(2)
>>> Q.extend([3, 4])
>>> Q.extendleft([5, 6])
>>> Q
deque([6, 5, 2, 1, 3, 4])
>>> Q.pop()
4
>>> Q.popleft()
6
>>> Q
deque([5, 2, 1, 3])
>>> Q.rotate(3)
>>> Q
deque([2, 1, 3, 5])
>>> Q.rotate(-3)
>>> Q
deque([5, 2, 1, 3])
'''
'''
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
a, b, x = 0, 1, 0
while b <= 4000000:
    if not b%2: x += b
    a, b = b, a+b
debug(x)'''
'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
def factors(n, prime=False):
    step = 2 if n%2 else 1
    if not prime:
        return sorted(list(set(x for tup in [[i, n//i] for i in range(1,
         int(n**0.5 + 1)) if not n%i] for x in tup)))
    else:
        return sorted(list(set(x for tup in [[i, n//i] for i in range(1,
         int(n**0.5 + 1)) if not n%i] for x in tup if isPrime(x))))
def isPrime(n):
  return len(factors(n)) == 2

facs = factors(600851475143, True)
debug(facs[-1])
ANSWER = 6857
'''
# Prime Number Check 1 - 100
for n in range(2, 101):
    for x in range(2, n):
        if n % x == 0: break
    else: debug(n)
'''
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
'''

# METACLASS Example
class meta(type):
    def __call__(self, **kwargs):
        obj = type.__call__(self)
        for k, v in kwargs.items():
            setattr(obj, k, v)
        return obj

class Person(metaclass=meta):
    @property
    def description(self):
        return ' '.join([str(i) for i in self.__dict__.values()])

tuna = Person(name='Tuna', surname='Durnal', gender='Male', birthPlace='World', birthDate='25/05/2005')
print(tuna.description)
