tc_kimlik_no = '11420348238'
for sayi in range(0,100):
    print(tc_kimlik_no)
    tc = int(tc_kimlik_no[:-2]) 
    if tc - 29999>0:
        tc_dokuz = str(tc - 29999).zfill(9)  
        onuncu = str((((int(tc_dokuz[0]) +int(tc_dokuz[2]) +int(tc_dokuz[4]) +int(tc_dokuz[6]) +int(tc_dokuz[8])) * 7 ) - (int(tc_dokuz[1]) + int(tc_dokuz[3])  + int(tc_dokuz[5]) + int(tc_dokuz[7])) ) % 10) 
        tc_on = tc_dokuz + onuncu 
        onbir = str((int(tc_on[0]) + int(tc_on[1]) + int(tc_on[2]) + int(tc_on[3]) + int(tc_on[4]) + int(tc_on[5]) + int(tc_on[6]) + int(tc_on[7]) + int(tc_on[8]) + int(tc_on[9]) ) % 10) 
        tc_kimlik_no = tc_on + onbir 