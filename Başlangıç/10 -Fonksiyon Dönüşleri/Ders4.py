# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama:  
from logo import logo
from clear import clear


def ekle(n1, n2):
  return n1 + n2

def cikar(n1, n2):
  return n1 - n2

def carp(n1, n2):
  return n1 * n2

def bol(n1, n2):
  return n1 / n2

islemler = {
  "+": ekle,
  "-": cikar,
  "*": carp,
  "/": bol
}

def hesaplayici():
  print(logo)

  sayi1 = float(input("İlk Sayıyı Giriniz!: "))
  for symbol in islemler:
    print(symbol)
  devammi = True
 
  while devammi:
    islem_sembolu = input("İşlem Seçiniz: ")
    sayi2 = float(input("İkinci Sayıyı Giriniz!: "))
    islem = islemler[islem_sembolu]
    cevap = islem(sayi1, sayi2)
    print(f"{sayi1} {islem_sembolu} {sayi2} = {cevap}")

    if input(f"{cevap} ile devam etmek için 'e' ye basınız , yeniden baslamak icin 'h' ye basınız: ") == 'y':
      sayi1 = cevap
    else:
      devammi = False
      clear()
      hesaplayici()

hesaplayici()

# ------------------------------------------------------------------