# ------------------------------------------------------------------
#Yönerge:  İç içe dizeler
#Çıktı:
#Uygulama: 
 
baskentler = {
  "Türkiye": "Ankara",
  "Fransa": "Paris",
  "Almanya": "Berlin",
}
print(baskentler)

#dize icinde liste

gezilen_sehirler = {
  "Fransa": ["Paris", "Lille", "Dijon"],
  "Almanya": ["Berlin", "Hamburg", "Stuttgart"],
}
print(gezilen_sehirler)

#dize icinde dize 
gezilen_sehirler = {
  "Fransa": {"sehirler": ["Paris", "Lille", "Dijon"], "ziyaret_sayisi": 12},
  "Almanya": {"sehirler": ["Berlin", "Hamburg", "Stuttgart"], "ziyaret_sayisi": 5},
}
print(gezilen_sehirler)

#Liste icinde dize 
gezilen_sehirler = [
{
  "ulke": "Fransa", 
  "sehirler": ["Paris", "Lille", "Dijon"], 
  "ziyaret_sayisi": 12,
},
{
  "ulke": "Almanya",
  "sehirler": ["Berlin", "Hamburg", "Stuttgart"],
  "ziyaret_sayisi": 5,
},
]
print(gezilen_sehirler)

def ziyaret_ekle(ulke, sehirler, ziyaret_sayisi):
    dize = {}
    dize["ulke"] = ulke
    dize["sehirler"] = sehirler
    dize["ziyaret_sayisi"] = ziyaret_sayisi
    gezilen_sehirler.append(dize)
    print(gezilen_sehirler)

ziyaret_ekle("İspanya",["Madrid", "Barcelona"], 4)
# ------------------------------------------------------------------