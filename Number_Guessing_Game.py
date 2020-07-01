import random
import time

print ("""
*************************
    SAYI TAHMİN OYUNU 
1-100 ARASI SAYI TAHMİN ET
*************************
""")

rastgelesayı = random.randint(1,100)
tahminhakkı = 7
while True:

    tahmin=int(input ("Tahmininiz:"))

    if (tahmin<rastgelesayı):
        print ("Sorgulanıyor...")
        time.sleep(1)
        print ("sayıyı yükselt")

        tahminhakkı-=1

    elif (tahmin>rastgelesayı):
        print ("Sorgulanıyor...")
        time.sleep(1)
        print ("sayıyı düşür")

        tahminhakkı-=1

    else:
        print("Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler", rastgelesayı)
        break
    if (tahminhakkı==0):
        print ("tahmin hakkınız bitti...")
        print ("sayımız:", rastgelesayı)


