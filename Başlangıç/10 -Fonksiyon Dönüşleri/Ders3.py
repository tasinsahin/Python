# ------------------------------------------------------------------
#Yönerge:  Artık Yıl Hesaplama
#Çıktı:
#Uygulama: 
def artik_yilmi_kontrolu(yil):    
    """Artık Yıl Mı Kontrol Eder""" #Döküman Dizisi 3 tırnak içinde
    artik_yilmi=False
    if yil % 4 == 0:
        if yil % 100 == 0:
            if yil % 400 == 0:
                artik_yilmi = True
            else:
                artik_yilmi = False
        else:
             artik_yilmi = False
    else:
        artik_yilmi = False
    return artik_yilmi


yil = int(input("Hangi yılı kontrol etmek istiyorsunuz?"))
artik_yilmi = artik_yilmi_kontrolu(yil)
if artik_yilmi == True:
    print(f"{yil} bir artık yıldır!")
else:
    print(f"{yil} bir artık yıl değildir!")

# ------------------------------------------------------------------