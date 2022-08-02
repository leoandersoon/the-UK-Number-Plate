plaka = input("Plakayı girin (GB) \t")

sayi = int(''.join(filter(str.isdigit, plaka)))

print(sayi)

if sayi >= 50:
    yil = sayi - 50
else:
    yil = sayi

if yil < 10:
        yil = 0+yil
else:
    pass

yil = str(yil)

print("Plakası girilen araç trafiğe 20"+yil+" tarihinde çıkmıştır.")