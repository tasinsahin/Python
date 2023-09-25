# ------------------------------------------------------------------
#Yönerge:  
#Çıktı: dd

#Uygulama:


class Araba:
    def __init__(self):
        print("Yeni bir araba oluşturuldu")

araba = Araba()
araba.model = "Honda"
araba.renk = "Kırmızı"
print(araba.model)
print(araba.renk)



class Motorsiklet:
    def __init__(self, model, renk):
        self.model = model
        self.renk  = renk
        print("Yeni bir motor oluşturuldu")

motor = Motorsiklet("BMW","Beyaz")
print(motor.renk)
print(motor.model)
print(motor.renk)


class Ev:
    def __init__(self,  renk):
        self.renk  = renk
        print("Yeni bir ev oluşturuldu")
    def renk_degistir(self, renk):
        self.renk = renk

ev = Ev("Beyaz")
print(ev.renk)
ev.renk_degistir("Mavi")
print(ev.renk)
# ------------------------------------------------------------------