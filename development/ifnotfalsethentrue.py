from datetime import datetime
# now == today
'''
%a:	hafta gününün kısaltılmış adı
%A:	hafta gününün tam adı
%b:	ayın kısaltılmış adı
%B:	ayın tam adı
%c:	tam tarih, saat ve zaman bilgisi == ctime()
%d:	sayı değerli bir karakter dizisi olarak gün
%j:	belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
%m:	sayı değerli bir karakter dizisi olarak ay
%U:	belli bir tarihin yılın kaçıncı haftasına geldiğini gösteren 0-53 arası bir sayı
%y:	yılın son iki rakamı
%Y:	yılın dört haneli tam hali
%x:	tam tarih bilgisi
%X:	tam saat bilgisi
x - saat
d - gün
'''
an = datetime.now()
print(datetime.ctime(an))
print(datetime.strftime(an, '%x'))
print(datetime.strftime(an, '%d.%m.%Y tarihinde buluşalım.')) # strptime tam tersine çevirir
'''
Hatırlarsanız os modülünü anlatırken stat() adlı bir fonksiyondan söz etmiştik. Bu fonksiyonun, dosyalar hakkında bilgi almamızı sağladığını biliyorsunuz:

>>> os.stat('dosya_adı')
Mesela bir dosyanın son değiştirilme tarihi öğrenmek için şöyle bir kod kullanıyorduk:

>>> os.stat('dosya_adı').st_mtime
st_mtime niteliği bize şuna benzer bir çıktı veriyor:

1417784445.8881965
Bu, içinde ayrıntılı tarih bilgisi barındıran bir zaman damgasıdır (timestamp). İşte bu zaman damgasını anlamlı bir tarih bilgisine dönüştürebilmek için datetime modülünün datetime sınıfı içindeki fromtimestamp() adlı fonksiyondan yararlanacağız:

>>> zaman_damgası = os.stat('dosya_adı').st_mtime
>>> tarih = datetime.datetime.fromtimestamp(zaman_damgası)
>>> tarih

datetime.datetime(2014, 12, 5, 15, 0, 45, 888196)
Bu şekilde bir datetime.datetime nesnesi elde ettikten sonra artık bu nesneyi istediğimiz şekilde manipüle edebiliriz. Mesela:

>>> datetime.datetime.strftime(tarih, '%c')

'12/05/14 15:00:45'
Demek ki 1417784445.8881965 zaman damgası, içinde ‘12/05/14 15:00:45’ tarihini barındırıyormuş.
FROMTIMESTAMP'''
''' TIMESTAMP - ZAMAN DALGASI URETIR FROMTIMESTAMP'IN TERSI
Eğer datetime.datetime nesnelerinden bir zaman damgası üretmek isterseniz timestamp() fonksiyonunu kullanabilirsiniz:

>>> tarih = datetime.datetime.now()
>>> zaman_damgası = datetime.datetime.timestamp(tarih)
>>> zaman_damgası

1417790594.558625
'''






















