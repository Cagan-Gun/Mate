def harf_notu_hesapla(vize,final):
    ortalama = vize * 4/10 + final * 6/10

    if ortalama >= 80:
        return [ortalama,"AA"]
    elif ortalama >= 70:
        return [ortalama,"BA"]
    elif ortalama >= 63:
        return [ortalama,"BB"]
    elif ortalama >= 53:
        return [ortalama,"CB"]
    elif ortalama >= 43:
        return [ortalama,"CC"]
    elif ortalama >= 40:
        return [ortalama,"DC"]
    elif ortalama >= 25:
        return [ortalama,"DD"]
    elif ortalama >= 10:
        return [ortalama,"FD"]
    else:
        return [ortalama,"FF"]

while(True):
    error = False
    vize_not = -1
    final_not = -1

    try:
        vize_not = int(input("Vize notu: "))
        final_not = int(input("Final notu: "))
        
    except ValueError:
        error = True
        print("Sayi giriniz!")

    if not error:
        if vize_not in range(0,101):
            if final_not in range(0,101):
                break
            else:
                print("Final notu 0 ile 100 arasinda olmalidir!")
        else:
            print("Vize notu 0 ile 100 arasinda olmalidir!")

ortalama = harf_notu_hesapla(vize_not,final_not)[0]
harf_notu = harf_notu_hesapla(vize_not,final_not)[1]

print(f"Ortalama: {ortalama} \nHarf notu: {harf_notu}")