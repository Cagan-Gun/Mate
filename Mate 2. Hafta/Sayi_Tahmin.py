from random import randint

Cevap = randint(1,100)

def Tahmin_et():
    while True:
        try:
            Tahmin = int(input("Tahmininiz: "))
            if Tahmin in range(1,101):
                return Tahmin
            else:
                print("1-100 arasinda bir sayi giriniz!")
        except ValueError:
            print("Bir sayi giriniz!")

Tahmini = Tahmin_et()

while Tahmini != Cevap:
    if Tahmini > Cevap:
        print("Assagi in")
    elif Tahmini < Cevap:
        print("Yukari cik")
    Tahmini = Tahmin_et()

print("Tahmin ettiniz!")