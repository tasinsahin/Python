print("Bir sayı giriniz : ")
num = int(input())

p = 0
i = 2
while i<num:
    if num%i == 0:
        p = 1
        break
    i = i+1

if p==0:
    print("\n" +str(num)+ " sayısı asal sayıdır.")
else:
    print("\n" +str(num)+ " sayısı asal sayı değildir.")