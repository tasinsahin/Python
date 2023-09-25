# ------------------------------------------------------------------
#Yönerge:  Pizaa fiyat hesaplayıcı
# Küçük Pizza : 15 TL
# Orta Pizza : 20 TL
# Büyük Pizza : 25 TL
# Ekstra Sos Küçük Pizza İçin : +2 TL
# Ekstra Sos Ora ve Büyük Pizza İçin : + 5 TL
#Ekstra Peynir : +3 TL
#Çıktı:
#Uygulama:
boy = input("Mezitli Pizzaya hoş geldiniz! Hangi Boy Pizza İstersiniz? K veya O veya B =>")
ekstraSos = input("Ekstra Sos İster misiniz? E veya H =>") 
ekstraPeynir = input("Ekstra Peynir İster misiniz? E veya H =>")
toplam = 0
if boy == "K":
    toplam += 15
elif boy == "O":
    toplam += 20
elif boy == "B":
    toplam += 25

if ekstraSos == "E":
    if boy == "K":
        toplam += 2
    else:
        toplam += 5
if ekstraPeynir == "E":
    toplam += 3

print(f"Toplam Ödeme = {toplam}")
# ------------------------------------------------------------------