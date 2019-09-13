'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''

'''
ALGORİTMA:

bir değişkene '0' ata
1000'den küçük 0'dan büyük sayıların içinde sırasıyla küçüten büyüğe dolaş
    olduğumuz sayının 3 veya 5 ile kalansız bölünebilmesini kontrol et
        bölünüyorsa sayıyı değişkene ekle 
'''

num = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0: num += i

print(num)

