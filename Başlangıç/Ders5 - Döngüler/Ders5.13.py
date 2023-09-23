# ------------------------------------------------------------------
#Yönerge:  Bir şifre oluşturucu kodu yazalım
#Çıktı:
#Uygulama: 
#Password Generator Project
import random
harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rakamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
semboller = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Şifre oluşturucuya hoşgeldiniz!")
harfSayisi = int(input("Şifrenizde kaç harf olsun?\n")) 
sembolSayisi = int(input(f"Şifrenizde kaç sembol olsun?\n"))
rakamSayisi = int(input(f"Şifrenizde kaç rakam olsun?\n"))
 
sifre = []

for char in range(1, harfSayisi + 1):
  sifre.append(random.choice(harfler))

for char in range(1, sembolSayisi + 1):
  sifre += random.choice(semboller)

for char in range(1, rakamSayisi + 1):
  sifre += random.choice(rakamlar)
 
random.shuffle(sifre) 

sifreYeni = ""
for char in sifre:
  sifreYeni += char

print(f"Şifreniz : {sifreYeni}")

# ------------------------------------------------------------------