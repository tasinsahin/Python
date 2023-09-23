# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama: 
import math

def boyaKutusuHesapla(yukseklik, genislik, kovaMetre):
    alan = yukseklik * genislik
    kovaAdedi = math.ceil(alan / kovaMetre)
    print(f"{kovaAdedi} kova boyaya ihtiyacınız var!")


yukseklik = int(input("Duvarın yüksekliğini giriniz (m) : "))
genislik = int(input("Duvarın genişliğini giriniz (m) : "))
kovaMetre = 5
boyaKutusuHesapla(yukseklik,genislik,kovaMetre)
# ------------------------------------------------------------------