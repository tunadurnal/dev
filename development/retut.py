import re
import functools as ft

ex = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''

names = re.findall(r'[A-Z][a-z]+', ex)
ages = re.findall(r'\d{1,3}', ex)

sozluk = dict(zip(names, ages))

print(re.findall(r'i.', ex))

for i in re.finditer('i.', ex):
    locStr = i.span()
    
    print(locStr)
    print(ex[ locStr[0]:locStr[1] ])

print(re.findall(r'[^J]*', ex))

ex = 'rat cat mat pat'
print(ex)
regex = re.compile('[^cr]at')
ex = regex.sub('tuna', ex)
print(ex)
ex = '<p>y utgrgufrytefyt</p>'
print(re.findall(r'<p>(.*?)</p>', ex))

if re.search('\w{2,20}\s\w{2,20}', 'Tuna Durnal'): print('Geçerli bir isim.')

ex = 'durnaltuna35@gmail.com'

if re.search('[\w.%+-]{1,20}@[\w.-]{2,20}.[A-Za-z{2,3}]', ex): print('Geçerli bir gmail adresi')
ex = "cat cats cat's"

print(re.findall(r"[cat]+['s]*", ex))

ex = '''Tuna Durnal is the best
I love him \r
And of course I want to date with that bad boy
'''
print(re.findall(r'[\w\s]+[\r]?', ex))
ex = '<name>Tuna Durnal</name><name>Zeynep Beceren</name>'
print(re.findall(r'<name>.*</name>', ex)) # Greedy Match
print(re.findall(r'<name>.*?</name>', ex)) # Lazy Match
ex = 'ape at the apex'
print(re.findall(r'\bape\b', ex)) # Word Baundaries
ex = 'Match everything up to @'
print(re.findall(r'^.*[^ @]', ex))
ex = '@ Get this string'
print(re.findall(r'[^@ ].*$', ex))
ex = '''Ape is big
Cheetah is fast
Turtle is slow'''
print(re.findall(r'(?m)^.*?\s', ex))
ex = 'Telefon numaram: 05053552506'
print(re.findall(r'0(.*)', ex)) # '0' hariç telefon numarasını alır
ex = '05056465500 05937285643 05127601925'
print(re.findall(r'0(.{10})', ex))
print(re.findall(r'0(.{3})(.{7})', ex))
print(re.findall(r'\d+', ex))
ex = 'the cat cat fell out the window'
print(re.findall(r'(\b\w+)\s+\1', ex))
ex = '<a href="#"><b>Arama Motoru</b></a>'
regex = re.compile(r'<b>(.*?)</b>')
ex = re.sub(regex, r'\1', ex)
print(ex)
ex = '412-555-1212'
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
ex = re.sub(regex, r'(\1)\2', ex)
print(ex)

ex = 'https://www.youtube.com http://www.google.com'
regex = re.compile(r'(https?://([\w.]+))')
ex = re.sub(regex, r'<a href="\1">\2</a>\n', ex)
print(ex)
ex = 'Bir iki üç dört'
print(re.findall(r'\w+(?=\b)', ex)) # Look Ahead
ex = '1. Ekmek 2. Marul 3. Yumurta 4. Elma 5. Portakal'
print(re.findall(r'(?<=\d.\s)\w+', ex)) # Look Behind
ex = '<h1>Ben önemliyim</h1> <h1>Yoksa değil miyim ?</h1>'
print(re.findall(r'(?<=<h1>).+?(?=</h1>)', ex)) # Look Ahead && Look Behind

ex = '8 Apples $3, 1 Bread $1, 1 Cereal $5'
ex = re.findall(r'(?<!\$)\d+', ex)
ex = [int(i) for i in ex]
print(ex)
print(ft.reduce((lambda x, y: x + y), ex))
ex = '1. Kedi 2. Köpek 3. At'
print(re.findall(r'\d\.\s(At|Köpek)', ex))
ex = '12345 12345-1234 1234 12346-333'
print(re.findall(r'(\d{5}\s|\d{5}-\d{3,4})', ex))

ex = '25-5-2005'
exRegex = re.search(r'(\d{1,2})-(\d{1,2})-(\d{4})', ex)

print('You were born on', exRegex.group())
print('Birth Month:', exRegex.group(1))
print('Birth Day:', exRegex.group(2))
print('Birth Year:', exRegex.group(3))

exRegex = re.search(r'\d{2}', 'Çocuk 25 kiloymuş.')
print('Match:', exRegex.group())
print('Span:', exRegex.span())
print('Start:', exRegex.start())
print('End:', exRegex.end())

ex = '13 Mart 2018'
regex = r'^(?P<gün>\d+)\s(?P<ay>\w+)\s(?P<yıl>\d+)'
matches = re.search(regex, ex)
print('Gün:', matches.group('gün'))
print('Ay:', matches.group('ay'))
print('Yıl:', matches.group('yıl'))

ex = 'd+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL'
print(re.findall(r'[\w_.+-]+@[\w-]+\.[\w.-]+', ex))

ex = '14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212'
regex = re.compile(r'((1?)(-| ?)(\()?(\d{3})(\)|-| |\)-|\))?(\d{3})(-| )?(\d{4}))')
matches = re.findall(regex, ex)
for i in matches: print(i[0].lstrip())
print(re.findall(r'[0-9\() ]+', ex))

















































      

