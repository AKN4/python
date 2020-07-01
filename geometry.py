talep=input("hangi sekil dörtgen veya ücgen: ")
if talep=="dörtgen":
    kenar1 = int(input("1. kenari giriniz: "))
    kenar2 = int(input("2. kenari giriniz: "))
    kenar3 = int(input("3. kenari giriniz: "))
    kenar4 = int(input("4. kenari giriniz: "))
    if (kenar1==kenar2==kenar3==kenar4):
        print("kare")
    elif (kenar1==kenar3 and kenar2==kenar4 and kenar1!=kenar2):
        print("dikdörtgen")
    else:
        print("cesitkenar")
elif talep=="ücgen":
    kenar1 = int(input("1. kenari giriniz: "))
    kenar2 = int(input("2. kenari giriniz: "))
    kenar3 = int(input("3. kenari giriniz: "))
    if kenar1+kenar2>kenar3 and kenar1+kenar3>kenar2 and kenar3+kenar2>kenar1:
        if kenar1==kenar2==kenar3:
            print("eskenar ücgen")
        elif kenar1==kenar2 or kenar1==kenar3 or kenar2==kenar3:
            print("ikizkenar ücgen")
        else:
            print("cesitkenar ücgen")
    else:
        print("girilen degerlerle ücgen olmaz")
else:
    print("yanlis girdiniz dörtgen veya ücgen")