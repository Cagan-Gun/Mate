while True:
    try:
        Sayi = int(input("Bir sayi giriniz: "))
        break
    except ValueError:
        print("Lutfen gecerli bir sayi giriniz!")

