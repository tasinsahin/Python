# ------------------------------------------------------------------
#Yönerge:  1 den 100'e kadar olan sayıları ekrana yazdırırken 3e bölünebilen sayılar yerine güç, 5e bölünebilenler yerine geç, ikisine de bölünebilenler için güçgeç yazan kodu yazalım
#Çıktı:
#Uygulama: 

for sayi in range(0, 100):
    if sayi % 3 == 0 and sayi % 5 == 0:
        print("güçgeç")
    elif sayi % 3 == 0:
        print("güç")
    elif sayi % 5 == 0:
        print("geç")
    else:
        print(sayi)
# ------------------------------------------------------------------