class Oyuncu():
    def __init__(self, isim, rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.güç = 0

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')

class Asker(Oyuncu):
    def __init__(self, *args):
        super().__init__(*args)
        self.guc = 100
    def hareket_et(self):
        super().hareket_et()
        print(f'{self.rutbe}, Hedefe ulaşıldı')

class Isci(Oyuncu):
    def __init__(self, *args):
        super().__init__(*args)
        self.guc = 70

class Yonetici(Oyuncu):
    def __init__(self, *args):
        super().__init__(*args)
        self.guc = 20

asker = Asker('Tuna', 'Kurmay Yüzbaşı')
asker.hareket_et()













        
