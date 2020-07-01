import math
import time

print("""

**********************
HESAP MAKİNESİ
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
5.Üs alma
6.Kök alma
7.Faktoriyel
8.EBOB
9.Çıkış için 9
**********************
""")

while True:
    işlem = int(input("Yapmak istediğiniz işlemi seçiniz:"))
    if işlem == 9:
        print("ÇIKILIYOR")
        break

    elif işlem == 1:
        sayı1 = int(input("Lütfen 1. sayıyı giriniz:"))
        sayı2 = int(input("Lütfen 2. sayıyı giriniz:"))
        print("Hesaplanıyor...")
        time.sleep(1)
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)
    elif işlem == 2:
        sayı1 = int(input("Lütfen 1. sayıyı giriniz:"))
        sayı2 = int(input("Lütfen 2. sayıyı giriniz:"))
        print("Hesaplanıyor...")
        time.sleep(1)
        print(sayı1, "-", sayı2, "=", sayı1 - sayı2)
    elif işlem == 3:
        sayı1 = int(input("Lütfen 1. sayıyı giriniz:"))
        sayı2 = int(input("Lütfen 2. sayıyı giriniz:"))
        print("Hesaplanıyor...")
        time.sleep(1)
        print(sayı1, "*", sayı2, "=", sayı1 * sayı2)
    elif işlem == 4:
        sayı1 = int(input("Lütfen 1. sayıyı giriniz:"))
        sayı2 = int(input("Lütfen 2. sayıyı giriniz:"))
        print("Hesaplanıyor...")
        time.sleep(1)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    elif işlem == 5:
        sayı1 = int(input("Lütfen üs almak istediğiniz sayıyı giriniz:"))
        sayı2 = int(input("Lütfen kaçıncı üs almak istediğinizi giriniz:"))
        print("Hesaplanıyor...")
        time.sleep(1)
        print(sayı1, "in", sayı2, ". üssü", sayı1 ** sayı2)
    elif işlem == 6:
        sayı1 = int(input("Lütfen kök almak istediğiniz sayıyı giriniz:"))
        sayı2 = int(input("Lütfen kaçıncı kök almak istediğinizi giriniz:"))
        print("Hesaplanıyor...")
        time.sleep(1)
        print(sayı1, "in", sayı2, "dereceden kökü", sayı1 ** (1 / sayı2))
    elif işlem == 7:
        sayı = int(input("Lütfen faktoriyel hesaplamak istediğiniz sayıyı giriniz:"))
        print("Hesaplanıyor...")
        time.sleep(1)
        print(sayı, "'nın faktoriyeli:", math.factorial(sayı))
    elif işlem == 8:
        sayı1 = int(input("Lütfen 1. sayıyı giriniz:"))
        sayı2 = int(input("Lütfen 2. sayıyı giriniz."))
        print("Hesaplanıyor...")
        time.sleep(1)
        print(sayı1, "ve", sayı2, "'nin EBOB'u", math.gcd(sayı1, sayı2))
    else:
        print("Yanlış işlem girdiniz...")






