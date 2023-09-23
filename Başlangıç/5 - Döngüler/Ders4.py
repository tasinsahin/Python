# ------------------------------------------------------------------
#Yönerge:  Girilen sayının faktoriyelini hesaplayan kodu yazalim
#Çıktı:
#Uygulama: 

girilenSayi = int(input("Bir sayı Giriniz!"))

carpim = 1

for sayi in range(1, girilenSayi+1):
    carpim *= sayi

print(f"Girdiğin sayının faktöriyeli : {carpim}")
# ------------------------------------------------------------------