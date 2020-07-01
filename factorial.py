print ("""
*******************************
Faktroriyel Bulma Programi 
(Cikmak icin q basin)
*******************************

""")


while True:
    sayi=input("bir sayi giriniz:")

    if sayi=="q":
        print("program sonlandiriliyor")
        break
    else:
        sayi=int(sayi)
        faktoriyel=1
        for i in range (2, sayi+1):
            faktoriyel=faktoriyel*i
        print("{}'nin faktroriyeli {}'dir.".format(sayi, faktoriyel))




