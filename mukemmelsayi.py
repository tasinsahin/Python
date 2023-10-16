print(end="Bir sayı giriniz : ")

num = int(input())
sum = 0
for i in range(1, num):
  if num%i==0:
    sum = sum+i
if num==sum:
  print("\n" + str(num) + " mükemmel sayı.")
else:
  print("\n" + str(num) + " mükemmel sayı değil.")