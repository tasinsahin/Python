# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama: 
print("Lunaparka hoşgeldiniz!")
boy = int(input("Boyunuz kaç cm ?"))
ucret =0
if boy >=  120:
    print("Rollercoastera binebilirsiniz!")
    yas = int(input("Kaç yaşındasınız?"))
    if yas < 12:
        ucret = 5
    elif yas <= 18:
        ucret = 10
    else:
        ucret = 20 
    fotografIstiyor = input("Fotoğraf çektirmek istiyor musunuz? E veya H")
    if fotografIstiyor == "E":
        ucret += 3
    print(f"Toplam ödeme: {ucret}") 
else:
    print("Üzgünüm, boyunuz rollercoastera binmek için yeterli değil!")
# ------------------------------------------------------------------