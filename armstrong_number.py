sayi=input("bir sayi giriniz:")
toplam=0
for i in sayi:
    toplam+=int(i)**(len(sayi))
if toplam==int(sayi):
    print(sayi, " bir armstrong sayidir")
else:
    print(sayi, " bir armstrong sayi degildir")



