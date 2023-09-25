# ------------------------------------------------------------------
#Yönerge:  Banka Şifresi Bulma
#Çıktı:
#Uygulama: 
sifre = "1234"
print("Mezitli Bankasına Hoşgeldiniz!")
sifreGirilen = input("Lütfen şifrenizi giriniz!")
if len(sifreGirilen) != 4:
    print("Eksik ya da fazla tuşladınız!")
elif sifre == sifreGirilen:
    print("Hoşgeldiniz!")
else:
    print("Yanlış tuşladınız!")
# ------------------------------------------------------------------