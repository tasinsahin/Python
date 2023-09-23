# ------------------------------------------------------------------
#Yönerge:  Vücut Kitle İndeksini Hesaplayan ve Yorum Yapan Kodu Yazalım
#Çıktı:
#Uygulama: 
boy  = float(input("Boyunuzu giriniz (m): "))
kilo = float(input("Kilonuzu giriniz (kg):"))

vki = int(kilo/boy**2)
if vki < 18.5:
    print(f"Vücut Kitle İndeksiniz: {vki} , Zayıfsınız!")
elif vki > 18.5 and vki < 25:
    print(f"Vücut Kitle İndeksiniz: {vki} , Kilonuz Normal")
elif vki > 25 and vki < 30:
    print(f"Vücut Kitle İndeksiniz: {vki} , Kilolusunuz")
elif vki > 30 and vki < 35:
    print(f"Vücut Kitle İndeksiniz: {vki} , Obezsiniz")
elif vki > 35:
    print(f"Vücut Kitle İndeksiniz: {vki} , Aşırı Kilolusunuz") 
# ------------------------------------------------------------------