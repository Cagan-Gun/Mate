while(True):
    error = False
    yas = -1

    try:
        yas = 2026 - int(input("Dogum yiliniz:"))
        
    except ValueError:
        error = True
        print("Sayi giriniz!")

    if not error:
        if yas in range(0,200):
            break
        print("Gecerli bir yil girin!")
        
if yas < 18:
    print("Ehliyet alamazsiniz")
else:
    print("Ehliyet alabilirsiniz")