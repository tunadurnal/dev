# class harfSayaci:
#     def __init__(self):
#         self.sesli_harfler = 'aeıioöuü'
#         self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
#         self.sesliSayac = 0; self.sessizSayac = 0
#     def start(self):
#         self.kelime = input('Bir kelime girin: ')
#         self.ekranaBas()
#     def ekranaBas(self):
#         sesli, sessiz = self.arttir()
#         mesaj = '{} kelimesinde {} tane sesli, {} tane sessiz harf bulunmaktadır.'
#         print(mesaj.format(self.kelime, self.sesliSayac, self.sessizSayac))
#     def arttir(self):
#         for harf in self.kelime:
#             if harf in self.sesli_harfler: self.sesliSayac += 1
#             else: self.sessizSayac += 1
#         return self.sesliSayac, self.sesliSayac          
# x = harfSayaci()
# x.start()
# class Çalışan():
#     personel = []

#     def __init__(self, isim):
#         self.isim = isim
#         self.kabiliyetleri = []
#         self.personele_ekle()

#     @classmethod
#     def personel_sayısını_görüntüle(cls):
#         print(len(cls.personel))

#     def personele_ekle(self):
#         self.personel.append(self.isim)
#         print(f'{self.isim} adlı kişi personele eklendi')

#     @classmethod
#     def personeli_görüntüle(cls):
#         print('Personel listesi:')
#         if cls.personel:
#             for kişi in cls.personel: print(kişi) 
#         else: print('Liste boş !')

#     def kabiliyet_ekle(self, kabiliyet):
#         self.kabiliyetleri.append(kabiliyet)

#     def kabiliyetleri_görüntüle(self):
#         print('{} adlı kişinin kabiliyetleri:'.format(self.isim))
#         for kabiliyet in self.kabiliyetleri:
#             print(kabiliyet)
        
# x = Çalışan('ahmet')
# x.personeli_görüntüle()

# class Sorgu():
#     def __init__(self, değer=None, sıra=None):
#         self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
#                       ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
#                       ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

#         if not değer and not sıra:
#             l = self.liste
#         else:
#             l = [li for li in self.liste if değer == li[sıra]]

#         for i in l:
#             print(*i, sep=', ')

#     @classmethod
#     def isbnden(cls, isbn):
#         cls(isbn, 0)

#     @classmethod
#     def yazardan(cls, yazar):
#         cls(yazar, 1)

#     @classmethod
#     def eserden(cls, eser):
#         cls(eser, 2)

#     @classmethod
#     def yayınevinden(cls, yayınevi):
#         cls(yayınevi, 3)
# print(Sorgu.eserden('Böyle Buyurdu Zerdüşt'))

# class matematik:
#     @staticmethod
#     def topla(a, b):
#         print(a+b)
# matematik.topla(1, 4)

class Calisan():
    _personel = []
    def __init__(self, isim):
        self._isim = isim
        self.personel_ekle()
    @property
    def isim(self):
        return self._isim
    @isim.setter
    def isim(self, yeni_isim):
        kisi = self._personel.index(self.isim)
        self._personel[kisi] = yeni_isim
        self._isim = yeni_isim
    def personel_ekle(self):
        self._personel.append(self._isim)
        print('{} adlı kişi personele eklendi'.format(self._isim))
    @classmethod
    def personel_goruntule(cls):
        print('Personel Listesi:')
        for kisi in cls._personel: print(kisi)

td = Calisan('KEko')
Calisan.personel_goruntule()
td.isim = 'Remzi'
Calisan.personel_goruntule()

























    
