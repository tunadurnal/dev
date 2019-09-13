import random
from functools import reduce

def mult_by_2(num):
    return num * 2

def do_math(func, num):
    return func(num)

def func_mult_by_num(num):
    def mult_by(value):
        return num * value
    return mult_by

def change_list(liste):
    oddList = [i for i in liste if i%2]
    return oddList

def annotation(isim: str, soyad: str, age: int, weight: float) -> str:
    return f'{isim} {soyad} {age} yaşında ve {weight} kilo.'

times_two = mult_by_2
print('2 * 8 =', times_two(8))
print('2 * 6 =', do_math(mult_by_2, 6))

generated_func = func_mult_by_num(5)
print('5 * 10 =', generated_func(10))

listOfFuncs = [do_math, generated_func]
print('5 * 9 =', listOfFuncs[1](9))

l = range(20)
print(change_list(l))

for i in range(1, 100):
    for b in range(2, int(i**0.5 + 1)):
        if not i%b: break
    else: print(i)

print(annotation('Tuna', 'Durnal', 13, 51))
print(annotation.__annotations__)

can_vote = lambda age: True if age >= 18 else False
print(can_vote(15), can_vote(77))

powerList = [lambda x: x**2,
            lambda x: x**3,
            lambda x: x**4]
for func in powerList: print(func(5))

attack = {'quick': (lambda: print('Quick Attack')), 'miss': (lambda: print('Missed Attack')),
          'power': (lambda: print('Power Attack'))}

attackKey = random.choice(list(attack.keys())) 
print('ATTACKKEY', attackKey)
attack[attackKey]()

l = random.choices(['H', 'T'], k=100)
print('Heads:', l.count('H'))
print('Tails:', l.count('T'))

print(list(filter((lambda x: not x%2), range(1, 6)))) # == print([i for i in [1,2,3,4,5] if i % 2 == 0])

print(list(filter((lambda x: not x%9), [random.randint(1, 1001) for i in range(100)])))
# reduce - map'ten farki listeye donusturme falan yapmamamız ve tek bir sonuç döndürmesi
print(reduce((lambda x, y: x + y), range(1, 6)))

