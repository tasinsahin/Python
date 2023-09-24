# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama: 
ogrenci_puanlari = {
  "Ali": 81,
  "Veli": 78,
  "Ayşe": 99, 
  "Fatma": 74,
  "Enes": 62,
} 
ogrenci_notlari = {} 
for ogrenci in ogrenci_puanlari:
  puan = ogrenci_puanlari[ogrenci]
  if puan > 90:
    ogrenci_notlari[ogrenci] = "A"
  elif puan > 80:
    ogrenci_notlari[ogrenci] = "B"
  elif puan > 70:
    ogrenci_notlari[ogrenci] = "C"
  else:
    ogrenci_notlari[ogrenci] = "Dersten Kaldı" 
print(ogrenci_notlari)
# ------------------------------------------------------------------