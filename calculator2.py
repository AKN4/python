import time
import math

print ("""
Hesap Makinesi Programı

1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Üs alma
6-Karekök
7-Faktoriyel
8-EBOB
9-çıkış

""")

while True:
    işlem=int(input ("Lütfen yapmak istediğiniz işlemi seçiniz:"))
    if işlem=="9":
        print ("çıkılıyor")
        time.sleep(1)
        break

    elif işlem==1:
        sy1=float(input ("1.sayıyı giriniz:"))
        sy2=float(input ("2.sayıyı giriniz:"))
        print ("Hesaplanıyor...")
        time.sleep(1)
        print ("Sonuç:",sy1+sy2)
    elif işlem==2:
        sy1=float(input ("1.sayıyı giriniz:"))
        sy2=float(input ("2.sayıyı giriniz:"))
        print ("Hesaplanıyor...")
        time.sleep(1)
        print ("Sonuç:",sy1-sy2)
    elif işlem==3:
        sy1=float(input ("1.sayıyı giriniz:"))
        sy2=float(input ("2.sayıyı giriniz:"))
        print ("Hesaplanıyor...")
        time.sleep(1)
        print ("Sonuç:",sy1*sy2)
    elif işlem==4:
        sy1=float(input ("1.sayıyı giriniz:"))
        sy2=float(input ("2.sayıyı giriniz:"))
        print ("Hesaplanıyor...")
        time.sleep(1)
        print ("Sonuç:",sy1/sy2)
    elif işlem==5:
        sy1=float(input ("Üssünü almak istediğiniz sayıyı giriniz:"))
        sy2=float(input ("Kaçıncı derece üs:"))
        print ("Hesaplanıyor...")
        time.sleep(1)
        print (math.pow (sy1,sy2))
    elif işlem==6:
        sy1=float(input ("Karekök almak istediğiniz sayıyı giriniz:"))
        print ("Hesaplanıyor...")
        time.sleep(1)
        print (math.sqrt (sy1))
    elif işlem==7:
        sy1=float(input ("Faktroiyel almak istediğiniz sayıyı giriniz:"))
        print ("Hesaplanıyor...")
        time.sleep(1)
        print (math.factorial (sy1))
    elif işlem==8:
        sy1=int(input ("1. sayıyı giriniz:"))
        sy2=int(input ("1. sayıyı giriniz:"))
        print ("Hesaplanıyor...")
        time.sleep(1)
        print (math.gcd (sy1,sy2))

    else:
        print ("yanlış işlem girdiniz...")