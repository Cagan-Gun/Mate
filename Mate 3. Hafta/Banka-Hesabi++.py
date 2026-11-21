class Banka_Hesabi:
    def __init__(self,Hesap_Sahibi="",Sifre="",Bakiye=0):
        self.Hesap_Sahibi = Hesap_Sahibi
        self.Sifre = Sifre
        self.Bakiye = Bakiye

    def Para_Yatir(self,Miktar):
        self.Bakiye += Miktar
        for i, Data in enumerate(Dosya_Data):
            if f"{self.Hesap_Sahibi} {self.Sifre}" in Data:
                Dosya_Data[i] = f"{self.Hesap_Sahibi} {self.Sifre} {self.Bakiye}\n"
        Dosya_Update()
        return f"Hesabiniza {Miktar}TL yuklendi, Yeni bakiyeniz: {self.Bakiye}TL\n"

    def Para_Cek(self,Miktar):
        self.Bakiye -= Miktar
        for i, Data in enumerate(Dosya_Data):
            if f"{self.Hesap_Sahibi} {self.Sifre}" in Data:
                Dosya_Data[i] = f"{self.Hesap_Sahibi} {self.Sifre} {self.Bakiye}\n"
        Dosya_Update()
        return f"Hesabinizdan {Miktar}TL cekildi, Yeni bakiyeniz: {self.Bakiye}TL\n"

    def Bilgi_ver(self):
        return f"Bakiyeniz: {self.Bakiye}TL"

def Dosya_Update():
    with open("Banka","w") as Dosya:
        for Data in Dosya_Data:
            Dosya.write(Data)

def Kosul_Kontrol(İnput_Yazi,Hata_Yazi,Alt_Sinir,Ust_Sinir):
    while True:
        try:
            Secenek = int(input(İnput_Yazi))
            if Secenek in range(Alt_Sinir,Ust_Sinir+1):
                return Secenek
            else:
                print(Hata_Yazi)
        except ValueError:
            print(Hata_Yazi)

def Hesap_Acma():
    Yeni_Hesap = Banka_Hesabi()
    Yeni_Hesap.Hesap_Sahibi = input("İsiminiz: ")
    for Data in Dosya_Data:
        if Yeni_Hesap.Hesap_Sahibi in Data.split():
            print("Bu isime sahip baska bir kullanici bulundu baska bir isimle deneyin!\n")
            return None
    Yeni_Hesap.Sifre = input("Sifreniz: ")
    with open("Banka","a+") as Dosya:
        Dosya.write(f"{Yeni_Hesap.Hesap_Sahibi} {Yeni_Hesap.Sifre} 0\n")
        Dosya_Data.append(f"{Yeni_Hesap.Hesap_Sahibi} {Yeni_Hesap.Sifre} 0\n")
    return Yeni_Hesap

def Giris_Yapma():
    Aranan_Hesap = Banka_Hesabi()
    Aranan_Hesap.Hesap_Sahibi = input("İsiminiz: ")
    Aranan_Hesap.Sifre = input("Sifreniz: ")
    for Data in Dosya_Data:
        if f"{Aranan_Hesap.Hesap_Sahibi} {Aranan_Hesap.Sifre}" in Data:
            Kullanici = Banka_Hesabi()
            Kullanici.Hesap_Sahibi = Data.split()[0]
            Kullanici.Sifre = Data.split()[1]
            Kullanici.Bakiye = int(Data.split()[2])
            return Kullanici
    print("Kullanici bulunamadi!\n")
    return None
    
Kullanici = Banka_Hesabi()
Giris = Kosul_Kontrol("(1) Hesap Acma, (2) Giris Yapma: ","1-2 arasinda bir sayi girin!\n",1,2)

with open("Banka","r") as Dosya:
    Dosya_Data = Dosya.readlines()

if Giris == 1:
    Kullanici = Hesap_Acma()
elif Giris == 2:
    Kullanici = Giris_Yapma()

if Kullanici:
    print("")
    print(Kullanici.Bilgi_ver())

    while True:
        İslem = Kosul_Kontrol("Ne yapmak istersiniz? (1) Para Yatirmak, (2) Para Cekmek, (3) Cikis Yapmak: ","1-3 arasinda bir sayi girin!\n",1,3)
    
        if İslem == 1:
            Miktar = Kosul_Kontrol(f"Yatirmak istediginiz tutar: ","1-100,000,000 arasinda bir sayi girin!\n",1,100000000)
            print(Kullanici.Para_Yatir(Miktar))
        elif İslem == 2:
            Miktar = Kosul_Kontrol(f"Cekmek istediginiz tutar: ",f"{Kullanici.Bakiye} den kucuk bir sayi girin!\n",0,Kullanici.Bakiye)
            print(Kullanici.Para_Cek(Miktar))
        elif İslem == 3:
            break