def indirim_hesapla(fiyat,indirim):
    indirim_tutari = fiyat * indirim / 100
    son_fiyat = fiyat - indirim_tutari
    return [indirim_tutari,son_fiyat]

while(True):
    error = False
    tam_fiyat = -1
    indirim_yuzde = -1

    try:
        tam_fiyat = float(input("Urunun tam fiyati: "))
        indirim_yuzde = float(input("Indirim yuzdesi: "))
        
    except ValueError:
        error = True
        print("Sayi giriniz!")

    if not error:
        if tam_fiyat > 0:
            if indirim_yuzde in range(0,101):
                break
            else:
                print("Indirim yuzdesi 0 ile 100 arasi olmak zorunda!")
        else:
            print("Fiyat 0'dan buyuk olmalidir!")

indirim_tutari = indirim_hesapla(tam_fiyat,indirim_yuzde)[0]
son_fiyat = indirim_hesapla(tam_fiyat,indirim_yuzde)[1]

print(f"Indirim tutari: {indirim_tutari} \nSon fiyat: {son_fiyat}")