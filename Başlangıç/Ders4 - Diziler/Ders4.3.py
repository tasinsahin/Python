# ------------------------------------------------------------------
#Yönerge: Hesabı kim ödeyecek oyununun kodunu yazalim  
#Çıktı:
#Uygulama: 
import random
isimler = "Şahin, Ali, Veli, Ahmet, Ayşe, Fatma"
isimDizisi = isimler.split(", ")
index = random.randint(0, len(isimDizisi) - 1 )

#print(f"Hesabı {random.choice(isimDizisi)} ödeyecek!")

print(f"Hesabı {isimDizisi[index]} ödeyecek!")
# ------------------------------------------------------------------