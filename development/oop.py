class DikKare:
    def __init__(self, height='0', width='0', kenar='0', ucgen1='0', ucgen2='0', ucgen3='0'):
        self.height = height
        self.width = width
        self.kenar = kenar
        self.ucgen1 = ucgen1
        self.ucgen2 = ucgen2
        self.ucgen3 = ucgen3
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print('Lütfen bir tam sayı girin.')
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print('Lütfen bir tam sayı girin.')
    @property
    def kenar(self):
        return self.__kenar
    @kenar.setter
    def kenar(self, value):
        if value.isdigit():
            self.__kenar = value
        else:
            print('Lütfen bir tam sayı girin.')
    @property
    def ucgen1(self):
        return self.__ucgen1
    @ucgen1.setter
    def ucgen1(self, value):
        if value.isdigit():
            self.__ucgen1 = value
        else:
            print('Lütfen bir tam sayı girin.')
    @property
    def ucgen2(self):
        return self.__ucgen2
    @ucgen2.setter
    def ucgen2(self, value):
        if value.isdigit():
            self.__ucgen2 = value
        else:
            print('Lütfen bir tam sayı girin.')
    @property
    def ucgen3(self):
        return self.__ucgen3
    @ucgen3.setter
    def ucgen3(self, value):
        if value.isdigit():
            self.__ucgen3 = value
        else:
            print('Lütfen bir tam sayı girin.')


    def KareAlanBul(self):
        return int(self.__kenar) * int(self.__kenar)
    def KareCevreBul(self):
        return 4 * int(self.__kenar)
    def DikAlanBul(self):
        return int(self.__width) * int(self.__height)
    def DikCevreBul(self):
        return (2 * int(self.__width)) + (2 * int(self.__height))
    def UcgenCevreBul(self):
        return int(self.__ucgen1) + int(self.__ucgen2) + int(self.__ucgen3)
    def UcgenAlanBul(self):
        return int(int(self.__width) * int(self.__height) / 2)
    def UcgenTurBul(self):
        if self.__ucgen1 == self.__ucgen2 == self.__ucgen3:
            print('\nNot: Bu bir eşkenar üçgen')
        elif self.__ucgen1 == self.__ucgen2 or self.__ucgen2 == self.__ucgen3 or self.__ucgen1 == self.__ucgen3:
            print('\nNot: Bu bir ikizkenar üçgen')
        else:
            print('\nNot: Bu bir çeşitkenar üçgen')

def cevapAl(ucgen=False):
    if ucgen:
        cevap = input('Bunlardan hangisi üçgenin taban uzunluğu ? (Çıkmak için q\'ya basın): ')
    else:
        cevap = input('Yukarıdakilerden birini seçin (Çıkmak için q\'ya basın): ')
    if cevap.lower() == 'q' or cevap.replace('İ', 'I').lower() == 'quit':
        quit()
    try:
        cevap = int(cevap)
    except ValueError:
        print('Hatalı bir giriş yaptınız !!')
        cevap = cevapAl()
    except:
        print('Beklenmedik bir hata meydana geldi')
        cevap = cevapAl()

    return cevap

def cevapKontrol(cevap, sayi):
    while not 0 < cevap < sayi:
        print('Lütfen sadece 0 ile {} arasında bir sayı girin.'.format(sayi))
        cevap = cevapAl()

    return cevap

def DikVSKare(cevap, sonradan=False, bastir=None):
    if cevap == 1:
        if sonradan:
            print(bastir)
        print('\n1) Çevre\n2) Alan\n3) İkisi de\n')
        calan = cevapKontrol(cevapAl(), 4)
        x = DikKare()
        kenar = input('Karenin bir kenarının uzunluğunu girin: ')
        x.kenar = kenar
        if calan == 1:
            print('Karenin çevresi:', x.KareCevreBul(), '\n')
        elif calan == 2:
            print('Karenin alanı:', x.KareAlanBul() , '\n')
        else: # calan == 3
            print('Karenin çevresi:', x.KareCevreBul())
            print('Karenin alanı:', x.KareAlanBul(), '\n')
    elif cevap == 2:
        if sonradan:
            print(bastir)
        print('\n1) Çevre\n2) Alan\n3) İkisi de\n')
        calan = cevapKontrol(cevapAl(), 4)
        x = DikKare()
        height = input('Dikdörtgenin yüksekliğini girin: ')
        width = input('Dikdörtgenin genişliğini girin: ')
        x.height = height
        x.width = width
        if calan == 1:
            print('Dikdörtgenin çevresi:', x.DikCevreBul(), '\n')
        elif calan == 2:
            print('Dikdörtgenin alanı:', x.DikAlanBul(), '\n')
        else: # calan == 3
            print('Dikdörtgenin çevresi:', x.DikCevreBul())
            print('Dikdörtgenin alanı:', x.DikAlanBul(), '\n')
    elif cevap == 3:
        if sonradan:
            print(bastir)
        print('\n1) Çevre\n2) Alan\n3) İkisi de\n')
        calan = cevapKontrol(cevapAl(), 4)
        if calan == 1:
            x = DikKare()
            ucgen1 = input('Üçgenin 1. kenarının uzunluğunu girin: ')
            ucgen2 = input('Üçgenin 2. kenarının uzunluğunu girin: ')
            ucgen3 = input('Üçgenin 3. kenarının uzunluğunu girin: ')
            x.ucgen1 = ucgen1
            x.ucgen2 = ucgen2
            x.ucgen3 = ucgen3
            print('Üçgenin çevresi:', x.UcgenCevreBul())
            x.UcgenTurBul()
        elif calan == 2:
            x = DikKare()
            height = input('Üçgenin  yüksekliğini girin: ')
            width = input('Üçgenin taban uzunluğunu girin: ')
            x.height = height
            x.width = width
            print('Üçgenin  alanı:', x.UcgenAlanBul())
            x.UcgenTurBul()
        else:
            x = DikKare()
            ucgen1 = input('Üçgenin 1. kenarının uzunluğunu girin: ')
            ucgen2 = input('Üçgenin 2. kenarının uzunluğunu girin: ')
            ucgen3 = input('Üçgenin 3. kenarının uzunluğunu girin: ')
            x.ucgen1 = ucgen1
            x.ucgen2 = ucgen2
            x.ucgen3 = ucgen3
            height = input('Üçgenin  yüksekliğini girin: ')
            print('\n1) {}\n2) {}\n3) {}\n'.format(ucgen1, ucgen2, ucgen3))
            ucCevap = cevapKontrol(cevapAl(True), 4)
            if ucCevap == 1:
                ucCevap = ucgen1
            elif ucCevap == 2:
                ucCevap = ucgen2
            else:
                ucCevap = ucgen3
            x.height = height
            x.width = ucCevap
            print('Üçgenin çevresi:', x.UcgenCevreBul())
            print('Üçgenin  alanı:', x.UcgenAlanBul())
            x.UcgenTurBul()

    else: # cevap == 4
        DikVSKare(1, True, 'Kare için;\n')
        DikVSKare(2, True, 'Dikdörtgen için;\n')
        DikVSKare(3, True, 'Üçgen için;\n')

print('**** Alan ve Çevre Bulan Program ****')
print('\n1) Kare\n2) Dikdörtgen\n3) Üçgen\n4) Hepsi\n')
cevap = cevapKontrol(cevapAl(), 5)
DikVSKare(cevap)
