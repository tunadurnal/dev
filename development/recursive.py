def factorial(num):
    if num == 1: return 1
    else:
        result = num * factorial(num - 1)
        return result

def fib(num):
    if num in (0, 1): return num
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

def cevapAl(objective):
    if objective == 'factorial':
    	cevap = input('Faktöriyelini bulmak istediğiniz sayıyı girin (Çıkmak için q\'ya basın): ')
    else:
        cevap = input('Fibonacci serisinin kaçıncı elemanını bulmak istediğinizi girin (Çıkmak için q\'ya basın): ')
    if cevap.lower() == 'q' or cevap.replace('İ', 'I').lower() == 'quit': quit()
    try: cevap = int(cevap)
    except: print('Hatalı bir giriş yaptınız !!'); cevap = cevapAl(objective)
    return cevap

def cevapKontrol(cevap, sayi, objective, fib=False):
    if fib:
        while cevap < 1:
            print('Lütfen 0\'dan büyük bir değer girin.')
            cevap = cevapAl(objective)
        if cevap >= sayi:
            onay = input('Normalde {}\'den daha büyük bir sayı girmeniz tavsiye edilmez ancak istiyorsanız y\'ye basın: '.format(sayi))
            if onay.lower() in ['y', 'yes', 'e', 'evet', 'yeah', 'evt']: return cevap
        else: return cevap
    else:
        while not 0 < cevap < sayi:
            print('Lütfen sadece 0 ile {} arasında bir sayı girin.'.format(sayi))
            cevap = cevapAl(objective)
        return cevap

def main():
    num = cevapKontrol(cevapAl('factorial'), 23, 'factorial')
    print('{}! = {}'.format(num, factorial(num)))
    num = cevapKontrol(cevapAl('fibonacci'), 100, 'fibonacci', True)
    print('{}. Fibonachi sayısı: {}'.format(num, fib(num)))

main()
