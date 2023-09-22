import math
# ------------------------------------------------------------------
#Yönerge:  Boy ve kilosunu giren kullanıcının ideal kilosuna ulaşması için alması veya vermesi gereken kiloyu hesaplayan kodu yazalım
#Çıktı:
#Uygulama: 
boy = float(input("Boyunuzu m cinsinden giriniz!"))
kilo = int(input("Kilonuzu kg cinsinden giriniz!"))

idealKilo = math.floor(22*boy*boy)
fark = abs(idealKilo-kilo)
if idealKilo > kilo:
    print(f"{fark} kilo almalısınız!")
else:
    print(f"{fark} kilo vermelisiniz!") 
# ------------------------------------------------------------------