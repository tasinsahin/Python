# ------------------------------------------------------------------
#Yönerge:  Ehliyet Alınabilirlik Sorgulama, 18 yaşından büyükse ve sağlıklı ise ehliyet alabilir
#Çıktı:
#Uygulama: 
yas = int(input("Kaç yaşındasın"))
if yas >= 18:
    saglik = input("Sağlıklı mısın? e veya h =>")
    if saglik == "e":
        print("Ehliyet Alabilirsin")
    else:
        print("Üzgünüm, Ehliyet Alamazsın")
else:
    print("Üzgünüm, Ehliyet Alamazsın")
# ------------------------------------------------------------------