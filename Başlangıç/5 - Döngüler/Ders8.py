# ------------------------------------------------------------------
#Yönerge:  Kullanıcının girdiği öğrenci boylarının ortalamasını bulan kodu yazalim
#Çıktı:
#Uygulama: 
boylar = input("Öğrenci boylarını cm cinsinden aralarında bir boşluk bırakarak giriniz!")
boyDizisi = boylar.split(" ")
toplam = 0
for boy in boyDizisi:
    toplam += int(boy)

print(f"Girilen boyların ortalaması : {toplam / len(boyDizisi)}")
# ------------------------------------------------------------------