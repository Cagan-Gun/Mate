from datetime import datetime

Suan = datetime.now()

while True:
    try:
        Tarih = input("(05/12/2026 19:30 gibi) Tarih ve Saat: ")
        Son_tarih = datetime.strptime(Tarih,"%d/%m/%Y %H:%M")
        if Son_tarih > Suan:
            break
        else:
            print("Gecmiste bir tarih girmeyiniz!")
    except ValueError:
        print("Formata gore giriniz!")

Fark = Son_tarih - Suan

Kalan_ay = Fark.days // 30
Kalan_gun = Fark.days % 30
Kalan_saat = Fark.seconds // 3600
Kalan_dakika = (Fark.seconds % 3600) // 60
Kalan_saniye = (Fark.seconds % 3600) % 60

print(f"Sinaviniza kalan sure: {Kalan_ay} ay {Kalan_gun} gun {Kalan_saat} saat {Kalan_dakika} dakika {Kalan_saniye} saniye")