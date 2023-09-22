# ------------------------------------------------------------------
#Yönerge: Kullanıcının yarıçapını, yüksekliğini girdiği silindirin alanı ve hacmini bulan kodu yazalım
#Çıktı:
#Uygulama:  
yaricap = input("Yarıçapı giriniz: ")
yukseklik = input("Yüksekliği giriniz: ")
pisayisi = 3.14
tabanAlani = pisayisi * yaricap * yaricap
tabanCevresi = 2 * pisayisi * yaricap
yanalAlan = yukseklik * tabanCevresi
toplamAlan = yanalAlan + (2 * tabanAlani)
hacim = tabanAlani * yukseklik 
print("Silindirin Hacmi: " + str(hacim))
print("Silindirin Alanı: " + str(toplamAlan))
# ------------------------------------------------------------------