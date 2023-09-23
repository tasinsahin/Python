alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, tekrarMiktari, encode_decode):
  sonuc = ""
  if encode_decode == "decode":
    tekrarMiktari *= -1
  for char in start_text: 
    if char in alfabe:
      index = alfabe.index(char)
      yeni_index = index + tekrarMiktari
      sonuc += alfabe[yeni_index]
    else:
      sonuc += char
  print(f"{encode_decode} sonucu : {sonuc}") 
from logo import logo
print(logo) 
sonlandır = False
while not sonlandır: 
  encode_decode = input("şifrelemek için 'encode' şifreyi çözmek için 'decode' yazınız:\n")
  text = input("Mesajınızı yazın :\n").lower()
  tekrar = int(input("Tekrar sayısını giriniz : \n")) 
  tekrar = tekrar % 26 
  caesar(start_text=text, tekrarMiktari=tekrar, encode_decode=encode_decode) 
  sonlandırmi = input("Devam etmek için 'evet', bitirmek için 'hayır' yazın! .\n")
  if sonlandırmi == "hayır":
    sonlandır = True
    print("Güle Güle!")
    


