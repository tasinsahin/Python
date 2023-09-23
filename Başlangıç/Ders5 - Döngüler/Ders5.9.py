# ------------------------------------------------------------------
#Yönerge:  Kullanıcının girdiği öğrenci puanlarından en yüksek ve en küçüğünü bulan programı yazalım
#Çıktı:
#Uygulama: 
puanlar = input("Öğrenci puanlarını arada bir boşluk olacak şekilde giriniz!")
enYuksekPuan = int(puanlar[0])
for puan in puanlar.split(" "):
    if enYuksekPuan < int(puan):
        enYuksekPuan = int(puan) 

print(f"En Yüksek Puan : {enYuksekPuan}")
print(f"En Küçük Puan : {min(puanlar.split(' '))}")
# ------------------------------------------------------------------