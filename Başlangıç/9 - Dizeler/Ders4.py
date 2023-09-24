# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama:  
import subprocess
from logo import logo
print(logo) 
peyler = {}
muzayede_bittimi = False 
def en_yuksek_peyverenkim(peyler):
  en_yuksek_pey = 0
  kazanan = "" 
  for peyveren in peyler:
    pey = peyler[peyveren]
    if pey > en_yuksek_pey: 
      en_yuksek_pey = pey
      kazanan = peyveren
  print(f"The kazanan: {kazanan} , peyi: ${en_yuksek_pey}") 
while not muzayede_bittimi:
  name = input("Adın Nedir?: ")
  pey = int(input("Pey Ne Kadar?: $"))
  peyler[name] = pey
  devammi = input("Başka pey veren var mı? Type 'evet or 'hayır'.\n")
  if devammi == "hayır":
    muzayede_bittimi = True
    en_yuksek_peyverenkim(peyler)
  elif devammi == "evet":
    command_to_execute = 'extension.clearTerminal'
    subprocess.run(['code', '--command', command_to_execute])
 
# ------------------------------------------------------------------