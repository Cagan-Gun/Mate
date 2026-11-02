while True:
    try:
        Son_sayi = int(input("Bir sayi giriniz: "))
        if Son_sayi > 0:
            break
        else:
            print("Pozitif bir sayi giriniz!")
    except ValueError:
        print("Sayi giriniz!")

Toplam = 0

for Sayi in range(1,Son_sayi+1):
    Toplam += Sayi

print(f"{Son_sayi}, 1 arasi toplam: {Toplam}")