# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama: 
def IsimDuzenle(isim, soyisim):
    isim = isim.title() 
    soyisim = soyisim.title() 
    isim_soyisim = isim + " " + soyisim
    return isim_soyisim

isim = input("İsminizi Girin!")
soyisim = input("Soyisminizi Girin!")
isim_soyisim = IsimDuzenle(isim, soyisim)
print(isim_soyisim)
# ------------------------------------------------------------------