# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama: 
# ------------------------------------------------------------------
sehirler  = [
"Adana","Adıyaman","Afyonkarahisar","Ağrı","Aksaray","Amasya","Ankara","Antalya","Ardahan","Artvin","Aydın","Balıkesir","Bartın","Batman",
"Bayburt","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Düzce","Edirne","Elazığ",
"Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Iğdır","Isparta","İstanbul","İzmir","Kahramanmaraş","Karabük",
"Karaman","Kars","Kastamonu","Kayseri","Kilis","Kırıkkale","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya",
"Malatya","Manisa","Mardin","Mersin","Muğla","Muş","Nevşehir","Niğde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Şanlıurfa",
"Siirt","Sinop","Şırnak","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli","Uşak","Van","Yalova","Yozgat","Zonguldak"
]
print(sehirler[0])
print(sehirler.index("Adana"))
print(sehirler[12])
print(sehirler[80]) 
print(sehirler[-1]) 
print(sehirler[-2]) 
sehirler[33] = "İçel"
print(sehirler[33])

sehirler.append("Tarsus")
print(sehirler[81])
print(len(sehirler))
sehirler.remove("Tarsus")
print(len(sehirler))
sehirler.pop()
print(len(sehirler))