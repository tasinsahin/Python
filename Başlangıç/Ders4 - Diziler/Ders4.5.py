# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama: 
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
harita = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

pozisyon = input("Hazineyi nereye koymak istersin?\n")

yatay = int(pozisyon[0]) -1
dikey = int(pozisyon[1]) - 1 
harita[dikey][yatay] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
# ------------------------------------------------------------------