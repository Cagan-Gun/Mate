while True:
    try:
        Baslangic = int(input("Bir sayi giriniz: "))
        if Baslangic > 0:
            break
        else:
            print("Pozitif bir sayi giriniz!")
    except ValueError:
        print("Sayi giriniz!")

for Adim in range(0,Baslangic+1):
    print(f"{Baslangic-Adim}",end=" ")
    
print("Atesle!")