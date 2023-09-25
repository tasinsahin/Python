# ------------------------------------------------------------------
#Yönerge:  


#Çıktı:
#Uygulama: 
import random
taş = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kağıt = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    kullaniciSecimi = int(input("Taş(0), Kağıt(1), Makas(2) seç!"))
    bilgisayarSecimi = random.randint(0,2)

    print("Senin Seçimin")
    if kullaniciSecimi == 0:
        print(taş)
    elif kullaniciSecimi == 1: 
        print(kağıt)
    elif kullaniciSecimi == 2: 
        print(makas)

    print("Bilgisayarın Seçimi")
    if bilgisayarSecimi == 0:
        print(taş)
    elif bilgisayarSecimi == 1: 
        print(kağıt)
    elif bilgisayarSecimi == 2: 
        print(makas)



    if kullaniciSecimi >=3 or kullaniciSecimi < 0:
        print("0 , 1 ,veya 2 giriniz!")
    elif kullaniciSecimi == 0 and bilgisayarSecimi == 2:
        print("Yendin!")
    elif bilgisayarSecimi == 0 and kullaniciSecimi == 2:
        print("Kaybettin!")
    elif kullaniciSecimi > bilgisayarSecimi:
        print("Yendin!")
    elif bilgisayarSecimi > kullaniciSecimi:
        print("Kaybettin!")
    else:
        print("Berabere!")
# ------------------------------------------------------------------