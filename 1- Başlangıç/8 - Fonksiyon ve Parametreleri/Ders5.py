# ------------------------------------------------------------------
#Yönerge:  Asal sayı kontrol eden fonksiyonu yazalım
#Çıktı:
#Uygulama: 

def asalSayiKontrol(sayi):
    asalSayimi = True
    for i in range(2, sayi):
        if sayi % i == 0:
            asalSayimi = False
        
    if asalSayimi:
        print("Girilen Sayı Asal Sayıdır!")
    else:
        print("Girilen Sayı Asal Değildir!")


sayi = int(input("Asal sayı kontrolü için sayı giriniz!"))
asalSayiKontrol(sayi)

# ------------------------------------------------------------------