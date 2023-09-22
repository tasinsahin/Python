# ------------------------------------------------------------------
#Yönerge:  Restoranda hesabı ödeyecek olan kullanıcının ne kadar bahşiş bırakacağını hesaplayan kodu yazalım.
#Çıktı:
#Uygulama: 
print("Bahşiş hesaplayıcıya hoşgeldiniz!")
hesap = float(input("Hesap ne geldi?"))
kisiSayisi = int(input("Kaç kişisiniz?"))
oran = float(input("Bahşiş oranı ne olsun?"))
toplam = hesap + (hesap*oran/100)
kisiBasi = toplam /kisiSayisi
print(f"Kişibaşı ödemeniz gereken tutar = {kisiBasi} TL")
# ------------------------------------------------------------------