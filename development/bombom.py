import os
import random
#import locale

tumce = 'Ben hafta içinde allahın her günü okula giderim.'.split()
print(tumce, '\n' +  ' '.join(tumce))

##word = input('Herhangi bir kelime: ')
##sayac = ''
##
##for harf in word:
##    if harf not in sayac:
##        if harf == ' ': print('"%s" kelimesinde %d tane boşluk var.' % (word, word.count((harf))))
##        else: print('%s harfi "%s" kelimesinde %d kez geçiyor.' % (harf, word, word.count((harf))))
##        sayac += harf

x = 'adana'

print(x.index('a'))
print(x.rindex('a'))
print(x.index('a', 3))
print(x.index('a', 1, 3))
print('**************************')
sayac = ''
for sayi in range(len(x)): # || range(list(enumerate(x))[-1][0])
    print('Sayı:', sayi)
    deal = str(x.index('a', sayi))
    if deal not in sayac:
        print(deal)
        sayac += deal
print('SON HAL HACI: ', sayac)
# YA DA:
for index in range(len(x)):
    if index == x.index('a', index): print(index)

# UYARI: index/rindex ve find/rfind arasındaki tek fark index bulamayınca hata verirken find bulamayınca -1 verir

x = 'Konuşaçağı kişinin adı: '
print(x.ljust(27, '.'))
print('5056554670'.zfill(11))
for i in range(11): print(str(i).zfill(2))

kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"
ceviriTablosu = str.maketrans(kaynak, hedef)
metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
print(metin.translate(ceviriTablosu))

metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
diyebiliriz."""

silinecek = "aeıioöuüAEIİOÖUÜ"
çeviri_tablosu = str.maketrans('', '', silinecek) #3. parametreye silinecek karakterleri içeren bir string verebiliriz
print(metin.translate(çeviri_tablosu))

# isalnum - hem alfabetik hem sayı içeren, isidentifier - tanımlanacak değişken yerine kullanılabilir mi
# ( python'daki özel kelimeler hariç ) ?
print('1Tr5ue'.isidentifier())
print('x  '.isspace())

# abs - mutlak değer, divmod - bir sayının bir sayıya bölünmesi işleminde bölüm ve kalan
print(abs(-5))
print(divmod(50, 5))
print(max('ashdöfg'))
print(max([1243, 323424, 35634, 24321, 346487534, 98654234]))

isimler = ["ahmet", "mehmet", "necla", "sedat", "abdullah", "gıyaseddin", "sibel", "can", "necmettin",
           "savaş", "özgür"]
print(max(isimler, key=len)) # Listedeki en uzun ismi bulmak
# min() - max'ın yaptığı işin tersini yapar
print(min(isimler, key=len))
# sum() - bir dizi içinde yer alan bütün sayıları birbiriyle toplar
print(sum([1243, 323424, 35634, 24321, 346487534, 98654234], 10)) # Sonuca 2. parametreyi de ekler
print((4.96).as_integer_ratio(), (12.0).is_integer(), (12.1).is_integer())

with open('new.txt', 'w') as f:
    print([x for x in dir(f) if not x.startswith('_')])
    print(f.closed, f.readable(), f.writable(), f.mode, f.name, f.encoding)
    
os.remove('new.txt')
print(repr('Ali topu tut !\n'))
harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
print({i: harfler.index(i) for i in harfler})
isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]
sozluk = {i: len(i) for i in isimler}
print(sozluk)
print(', '.join(sozluk.keys()), tuple(sozluk.values()), sozluk.items(),
      sozluk.get('ali', 'Bu kelime veritabanımızda yoktur!')) # clear(), copy()
print(dict.fromkeys(("Ahmet", "Mehmet", "Can"), 'Kadıkoy'))
print(sozluk.pop('mehmet', 'silinecek öğe yok'), sozluk.pop('tuna', 'silinecek öğe yok'))
print(sozluk.popitem()) # Herhangi rastgele bir öğeyi siler
print(sozluk.setdefault('ayşe', len('ayşe'))) # Normal atama yapar.
sozlukTemp = sozluk.copy()
sozlukTemp['fırat'] = 'sana ne'
sozluk.update(sozlukTemp); del sozlukTemp # Sözlüğü başka valulerle günceller
print(sozluk)
liste = ["elma", "armut", "elma", "kiraz", "çilek", "kiraz", "elma", "kebap"]
print({i: liste.count(i) for i in set(liste)})
liste = [random.randint(0, 1000) for i in range(1000)]
kume = {i for i in liste if i < 100}
print(kume)
print([i for i in dir(set) if not i.startswith('_')])
# clear(), copy()
kume.add(100)
print(kume)
k1 = set([1, 2, 3, 5])
k2 = set([3, 4, 2, 10])
print(k1.difference(k2), k1-k2, k2.difference(k1), k2-k1) # Birinde olup diğerinde olmayan
k1.difference_update(k2) # k1 -= k2 Farkını bulduğun şeye eşitle
print(k1)
# discard() == remove() ama remove hata verebilir discard hata vermez
k1.discard(55)
k1.remove(1)
print(k1)
k1 = set([1, 2, 3, 4])
k2 = set([1, 3, 5, 7])
print(k1.intersection(k2), k1 & k2) # Kesişim ( Ortak  Elemanlar )

tr = "şçöğüıŞÇÖĞÜİ"
parola = 'çilek'
if set(tr) & set(parola): print('Parolanızda Türkçe harfler kullanmayın !')
else: print('Parolanız kabul edildi')
# intersection_update() &=
# isdisjoint() kesişim yok mu ? ( Kümeler ayrık mı ? )
print(k1.isdisjoint(k2)) # False -->> Kümelerin kesişen en az bir elemanı var
print(k1.issubset(k2)) # İlk kümedeki tüm elemanlar diğerinde de var mı ?
print(k2.issuperset(k1)) # İkinci kümedeki elemanlar ilkinde var mı ?
print(k1.union(k2), k1 | k2) # Kümeleri birleştir
# update() listelerdeki 'extend()' gibi örneğin başka bir liste veriyoruz ve onun içindeki elemanları atıyor
k1.update('Biraz gevşemen lazım bu stresle yaşanmaz.'.split())
print(k1)
print(k1.symmetric_difference(k2)) # ^ İkisinde aynı olmayan elemanlar
# symmetric_difference_update() ^=
# pop() rastgele öğe siler ve sildiğini döndürür
# frozenset() değiştirilemeyen kümeler ( dondurulmuş ) normalinden tek farkı add(), remove(), update() gibi şeyler yok
print(abs(-89)) # Mutlak Değer
print(round(5.5), round(12.5), round(55/3, 5)) # .5 olunca en yakın çift tam sayıya yuvarlar 2. parametre hassasiyet
# all() dizideki 1 eleman False ise False, hepsi True ise True döndürür.
print(all([5,6]), all([4,0,6,8]), all(['a', '', 'naber']))
# any() all()'un tam tersi dizideki 1 eleman True ise True, hepsi False ise False döndürür.
print(any([0, 5]))
'''ascii() olayları Python'un bakış açısına göre yorumlar '\n' gibi, buna verilen liste yeni değişkende artık
string olmuştur.'''
l = ['kiraz', 'çeşme', 'elma', 'armut']
print(ascii('\nnaber'), ascii(l), type(ascii(l)))
# repr() ascii()'den tek farkı yabancı harf gördüğünde onu da olduğu gibi bastırmasıdır
print(repr('\nnaber'), repr(l), type(repr(l)))
# callable() parametredeki şeyin çağrılabilir olup olmadığını denetler ( değişkenler çağırılamaz, fonklar çağırılır )
print(callable(callable), callable(l))
'''eval() ifadeleri çalıştırır, exec() ifade && deyimleri çalıştırır Örnek: değişken atama bir deyimdir
globals() çok havalı bir fonksiyon. Dışarı dünyaya ait tüm değişkenleri vb sözlük şeklinde tutar.
En iyi kısım ise o sözlüğe bir değer ekleyebilirsiniz ! '''
#print(globals())
globals()['tuna'] = 'programmer'
print(tuna)
# locals globals()'dan tek farkı fonksiyon veya sınıf içindeki lokal değişkenleri tutması. Onun dışında kullanım aynı.
def fonk(p1, p2):
    x = 10; print(locals())
    
fonk('naber', 'aga')
# globals() gibi bir sözlük oluşturup exec() ile onun içine de atama yapabilirsiniz ve gerçek değer korunmuş olur.
num = 31
var = {}; exec('num = 50', var); print(num, var['num'])
# exit() Just closes your programme, keep it simple :)
# id() her nesnenin bir kimliği vardır bu da onu yazdırır aslında birazcık enteresan; Sanaaa numaraa verdiler mi ?
print(id('bhsdfhyua'), id(6))
'''filter() - çok kullanışlı, işe yarar ve bilinmesi gereken bir fonk 2. parametre 'map edilecek' listeyi alır,
1. Parametre ne yapılması gereken fonksiyon verilir.
'''
notlar = {'Ahmet'   : 60,
          'Sinan'   : 50,
          'Mehmet'  : 45,
          'Ceren'   : 87,
          'Selen'   : 99,
          'Cem'     : 98,
          'Can'     : 51,
          'Kezban'  : 100,
          'Hakan'   : 66,
          'Mahmut'  : 80}

# hadi gelin 70'ten büyük veya eşit olan notların sahiplerini ekrana bastıralım
def fo(num):
    if num >= 70: return num
# NOTLAR: print('FUCKING PAY ATTENTION', *filter(lambda x: x >= 70, notlar.values()))
# SAHIPLER:
for i in notlar.items():
    if i[1] >= 70: print(i[0].ljust(10), i[1])

print(isinstance(4.5, float), isinstance('hello', int))
print(list(map(lambda x:x**2, [1,2,3,4,5])))
def en_yuksek_rutbe(rutbe):
    rutbeler = {'er'        : 0,
                'onbaşı'    : 1,
                'çavuş'     : 2,
                'asteğmen'  : 3,
                'teğmen'    : 4,
                'üsteğmen'  : 5,
                'yüzbaşı'   : 6,
                'binbaşı'   : 7,
                'yarbay'    : 8,
                'albay'     : 9}

    return rutbeler[rutbe]

askerler = {'ahmet': 'onbaşı',
            'mehmet': 'teğmen',
            'ali': 'yüzbaşı',
            'cevat': 'albay',
            'berkay': 'üsteğmen',
            'mahmut': 'binbaşı'}

#print(max(askerler.values(), key=en_yuksek_rutbe))
for k, v in askerler.items():
    if askerler[k] in max(askerler.values(), key=en_yuksek_rutbe): print(v, k) # in || ==
print(pow(2, 6, 12)) # 1. parametre == sayı, 2. p == kacinciKuvvet, 3. p(Opsiyonel)== sonuc % 3.p (bölümünden kalanı)
print(*range(0, 100, 3)) # 3.p atlama değeri -üçer üçer say-
print(list(reversed([1,2,3,4])))
print(sorted('tuna')) # her harfini alfabetik sıraya dizdi
#locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
isimler = ['ahmet', 'çiğdem', 'ışık', 'şebnem', 'zeynep', 'selin']
random.shuffle(isimler)
#print(sorted(isimler, key=locale.strxfrm)) # Sıralamada tr karakter
# Ama hala i ı'dan önce geliyor. Yani bundan bir cacık olmaz :) Hadi gelin kendi sıralama mekanizmamızı icat edelim:
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
translator = {i: harfler.index(i) for i in harfler}
# print(sorted(isimler, key=lambda x: translator.get(x[0]))) # Sadece ilk harflerine göre sıralar
print('*************************************\n')
# Tum harflere gore siralyor muhtesem bir sey !
def order(word):
    return [translator.get(i) for i in word]
print(*sorted(isimler, key=order), sep=' *\n', end=' *\n')

yazi = '''Merhaba, benim adım %(ad)s. Adımın %(ad)s olmasından memnunum çünkü türkçe karakter içermiyor, kısa ve öz.
Aynı zaman %(ad)s diye bir nehir bile var ! '''
print(yazi % {'ad':'Tuna'})
print('%d' % 56.0)  
print('%05d' % 12) # başına sıfır koyarsak boşlukları 0'la doldurur
print("%.2f" % 10) # .2 ->> noktadan sonra kaç rakam olacak
print('%10.5d' % 45) # 10 = toplam uzunluk, .5 = 4. indis(5.)'den sonra 0 ile doldurmaya başla örnek:"%-10.5d" %10
print('%c' % 't', '%c' % 90) # c - char & ACII
for i in range(128): print('%s ==>> %c' % (i, i), end=' ') # ACII tablosu
print('\nKonumuz: {konu}'.format(konu = 'Matematik'))
print('|{:^15}|'.format('tuna')) # : - biçimlendirme olacağını gösterir, < sola, > sağa, ^ ortalar (yaslar) 15 ne kadar
# ÖNEMLİ :: %'de %s str veya str'ye cevirilebilen her sey, format'ta :s sadece str
print('{:s} ile {:s} iyi bir ikilidir.'.format('Python', 'Django'))
''':c ASCII, :d tam sayı, :o (%'de de %o var) ondalıktan sekizlik düzene çevirir x on-on altı, X x'ten farkı ondalık
düzende olup da on altılıkta olmayanlara karşılık gelen sayıları (a,b,c...) büyük yazar, b on-iki, f float,
"," basamak ayracı
'''
# Onlu Sayma Sistemi
print((0 * (10 ** 0)) + (8 * (10 ** 1)) + (9 * (10 ** 2)) + (1 * (10 ** 3))) # 1980
# sekizli Sayma Sistemi
sayı_sistemleri = ["onlu", "sekizli"]
print(("{:^5} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
for i in range(17): print("{0:^5} {0:^5o}".format(i))
print((4*(8**0)) + (7*(8**1)) + (6*(8**2)) + (3*(8**3))) # 1980
print('%o' % 1980)
'''On Altılı Sayma Sistemi
normalde onlu sistem tüm rakamları tamamen kapsar yani on altıda diğer altı şey a,b,c,d,e... diye isimlendirilir.
0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,10 // bu arada sonraki a,b,c,d... için 1a,1b sonra 2a,2b gibi kullanılacak
Aslında bu sistem onlu sistem + 6 pas gibi bir şey
İlk on simge, onluk sayma sistemindekilerle aynı. Ancak 10‘dan sonraki sayıları gösterebilmek için elimizde başka
simge yok. On altılık sistemi tasarlayanlar, bir tercih sonucu olarak, eksik sembolleri alfabe harfleriyle tamamlamayı
tercih etmişler. Alfabe harfleri yerine pekala Roma rakamlarını da tercih edebilirlerdi. Eğer bu sistemi tasarlayanlar
böyle tercih etmiş olsaydı bugün on altılık sistemi şöyle gösteriyor olabilirdik:
0
1
2
3
4
5
6
7
8
9
I
II
III
IV
V
VI
Bugün bu sayıları bu şekilde kullanmıyor olmamızın tek sebebi, sistemi tasarlayanların bunu böyle tercih etmemiş
olmasıdır...'''
sayı_sistemleri = ["onlu", "sekizli", "on altılı"]
print(("{:^8} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
for i in range(17): print("{0:^8} {0:^8o} {0:^8x}".format(i))
'''Mesela 7bc sayısının ondalık sistemdeki karşılığı 1980 :D Peki harfleri nasıl kullanacağız ? Şöyle bir şey
yapabiliriz:
a –> 10
b –> 11
c –> 12
d –> 13
e –> 14
f –> 15 O zaman bu şu şekilde hesaplayabiliriz:'''
print(((12 * (16 ** 0)) + ((11 * (16 ** 1)) + ((7 * (16 ** 2))))), '%x'%1980)
n = '7bc'
print("{} sayısının onlu karşılığı {} sayısıdır.".format(n, int(n, 16))) # int()'e verilen 2. parametre sayma sistemi
# İkili Sayma Sistemi (binary) sistemi : 0, 1
sayı_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]
print(("{:^9} "*len(sayı_sistemleri)).format(*sayı_sistemleri))
for i in range(17): print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))
print((0 * (2 ** 0)) + (0 * (2 ** 1)) + (1 * (2 ** 2)) + (1 * (2 ** 3))) # 1100 ==>> onluk sistemde 12
# Sayma Sistemlerini Birbirine Dönüştürme
print(bin(12), bin(12)[2:]) # on-iki baştaki 0b o sayının ikili sayma sisteminden olduğunu gösterir. 
print(hex(10)) # on-on altı baştaki 0x sayının on altılı sayma sisteminden oluştuğunu gösterir
print(oct(10)) # on-sekiz 0o == sayı sekizlik sayma sisteminden
# Fark ettiyseniz 0b, 0x, 0o'lar aslında biçimlendirmede de (0'dan sonraki harfi) direkt kullandığımız bir yapı
print(int('7bc', 16)) # 2. parametre == sayının sayma sistemi. Neticede onluk sayma sistemine dönüştürür
# format'ta :b on-iki (bin() gibi)
print(int('ff', 16))
print(len(bin(10)[2:]) == (10).bit_length())
for i in range(2**8): print(bin(i)[2:].zfill(8))














































