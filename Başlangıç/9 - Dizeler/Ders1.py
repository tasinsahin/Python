# ------------------------------------------------------------------
#Yönerge:  
#Çıktı:
#Uygulama: 
# Dize oluşturma
dize1 = {}
print(dize1)

#dizeye eleman ekleme
dize1["eleman1"] = "Ben bir dizedeyim"
print(dize1)
#{'eleman1': 'Ben bir dizedeyim'}

dize1["eleman2"] = "Ben de bir dizedeyim"
print(dize1)
#{'eleman1': 'Ben bir dizedeyim', 'eleman2': 'Ben de bir dizedeyim'}

dize1["eleman1"] = "Ben değiştirildim"
print(dize1)
#{'eleman1': 'Ben değiştirildim', 'eleman2': 'Ben de bir dizedeyim'}

for eleman in dize1:
    print(eleman)
    print(dize1[eleman])

# ------------------------------------------------------------------