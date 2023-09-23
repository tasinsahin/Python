# ------------------------------------------------------------------
#Yönerge:  Sevgi Ölçer
#Çıktı:
#Uygulama: 
print("Sevgi Hesaplayıcıya hoş geldiniz!")
isim1 = input("Adınız Nedir?")
isim2 = input("Onun Adı Nedir?")

isimler = ( isim1 + isim2 ).lower()

g = isimler.count("g")
e = isimler.count("e")
r = isimler.count("r")
ç = isimler.count("ç")
e = isimler.count("e")
k = isimler.count("k")
a = isimler.count("a")
ş = isimler.count("ş")
k = isimler.count("k")

toplam = g + e + r + ç + e + k + a + ş + k

if( toplam < 10 and toplam > 90):
    print(f"Sevgi Puanınız: {toplam}, kola mentos gibisiniz!") 
elif( toplam > 40 and toplam < 50):
    print(f"Sevgi Puanınız: {toplam}, beraber iyisiniz!")
else:
    print(f"Sevgi Puanınız: {toplam}") 

# ------------------------------------------------------------------