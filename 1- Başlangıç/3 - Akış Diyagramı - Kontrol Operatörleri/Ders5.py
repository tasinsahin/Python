# ------------------------------------------------------------------
#Yönerge:  Artık Yıl Hesaplama
#Çıktı:
#Uygulama: 
yil = int(input("Hangi yılı kontrol etmek istiyorsunuz?"))
if yil % 4 == 0:
    if yil % 100 == 0:
        if yil % 400 == 0:
            print(f"{yil} bir artık yıldır!")
        else:
            print(f"{yil} bir artık yıl değildir!.")
    else:
         print(f"{yil} bir artık yıl değildir!.")
else:
    print(f"{yil} bir artık yıl değildir!.")
# ------------------------------------------------------------------