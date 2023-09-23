import random
from hangman_kelimeler import kelimeler
from hangman_sahneler import logo
print(logo)
secilenKelime = random.choice(kelimeler)
kelimeUzunlugu = len(secilenKelime)
oyunBitti = False
canlar = 6 
goruntu = []
for _ in range(kelimeUzunlugu):
    goruntu += "_"
while not oyunBitti:
    guess = input("Bir harf tahmin et: ").lower()
    if guess in goruntu:
        print(f"Daha önce denedin, {guess}")
    for index in range(kelimeUzunlugu):
        harf = secilenKelime[index]
        if harf == guess:
            goruntu[index] = harf
    if guess not in secilenKelime:
        print(f"{guess} kelimede yok. Bir can kaybettin!")
        canlar -= 1
        if canlar == 0:
            oyunBitti = True
            print("Kaybettin.")
    print(f"{' '.join(goruntu)}")
    if "_" not in goruntu:
        oyunBitti = True
        print("Kazandın!")
    from hangman_sahneler import sahneler
    print(sahneler[canlar])
    print(f"Tahmin etmen gereken kelime {secilenKelime} idi.")