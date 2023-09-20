# ------------------------------------------------------------------
#Yönerge:  Vücut Kitle İndeksini Hesaplayan Kodu Yazalım
#Çıktı:
#Uygulama: 
boy  = float(input("Boyunuzu giriniz (m): "))
kilo = float(input("Kilonuzu giriniz (kg):"))

vki = int(kilo/boy**2)
print("Vücut Kitle İndeksiniz: " + str(vki))
# ------------------------------------------------------------------