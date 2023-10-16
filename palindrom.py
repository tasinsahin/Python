metin = input('Metni Girin : \n')
ters=metin[::-1]

print('Girilen metnin tersi = %s' % (ters))
if ters == metin:
    print('Girilen metin palindrom')
else:
    print('Girilen metin palindrom değil.')