anapara = float(input("Anapara (TL): "))
aylik_faiz_orani = (float(input("Yıllık Faiz Oranı (%): ")) / 100) /12
vade = int(input("Vade (ay): ")) 
aylik_taksit = (anapara * aylik_faiz_orani * (1 + aylik_faiz_orani)**vade) / ((1 + aylik_faiz_orani)**vade - 1)
toplam_geri_odeme = aylik_taksit * vade
print("Aylık Taksit:", round(aylik_taksit, 2), "TL")
print("Toplam Geri Ödeme:", round(toplam_geri_odeme, 2), "TL")