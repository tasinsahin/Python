# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama: 
print("Lunaparka hoşgeldiniz!")
print("Bilet fiyatı yetişkin 10 TL. 12 yaşından küçükler 5 TL")
boy = int(input("Lütfen boyunuzu giriniz!(cm)"))
yas = int(input("Lütfen yaşınızı giriniz."))
biletfiyati = 0
if boy > 80 :
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati = 10
    print(f"Çarpışan Arabalara binebilirsiniz! Fiyat {biletfiyati} TL")
elif boy > 80 and boy < 120:
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati = 10
    print(f"Lunapark Hız Trenine binebilirsiniz! Fiyat {biletfiyati} TL")
elif boy > 120 and boy < 140:
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati = 10
    print(f"Gondola binebilirsiniz! Fiyat {biletfiyati} TL")
elif boy > 140:
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati = 10
    print(f"Kamikazeye binebilirsiniz! Fiyat {biletfiyati} TL")
else:
    print("Lunaparkta herhangi bir araca binmek için boyunuz yetmiyor!")


# ------------------------------------------------------------------