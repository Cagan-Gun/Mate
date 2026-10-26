def indirim_hesapla(fiyat,indirim):
    indirim_tutari = fiyat * indirim / 100
    son_fiyat = fiyat - indirim_tutari
    return [indirim_tutari,son_fiyat]

tam_fiyat = float(input("Urunun tam fiyati: "))
indirim_yuzde = float(input("Indirim: "))

indirim_tutari = indirim_hesapla(tam_fiyat,indirim_yuzde)[0]
son_fiyat = indirim_hesapla(tam_fiyat,indirim_yuzde)[1]

print(f"Indirim tutari: {indirim_tutari} \nSon fiyat: {son_fiyat}")