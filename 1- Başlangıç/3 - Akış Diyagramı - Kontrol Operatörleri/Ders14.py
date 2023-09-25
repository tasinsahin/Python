# ------------------------------------------------------------------
#Yönerge:  Kullanıcının girdiği 5 sayının en büyüüğünü bulan kodu yazalım
#Çıktı:
#Uygulama: 
sayi1 = int(input("1nci Sayıyı Giriniz!"))
sayi2 = int(input("2nci Sayıyı Giriniz!"))
sayi3 = int(input("3nci Sayıyı Giriniz!"))
sayi4 = int(input("4nci Sayıyı Giriniz!"))
sayi5 = int(input("5nci Sayıyı Giriniz!"))
enBuyuk = sayi1

if enBuyuk < sayi2:
    enBuyuk  = sayi2
if enBuyuk < sayi3:
    enBuyuk  = sayi3
if enBuyuk < sayi4:
    enBuyuk  = sayi4
if enBuyuk < sayi5:
    enBuyuk  = sayi5 

print(f"Girilen Sayılardan En Büyüğü = {enBuyuk}")

# ------------------------------------------------------------------