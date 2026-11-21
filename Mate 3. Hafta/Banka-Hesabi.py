class Banka_Hesabi:
    def __init__(self,Hesap_Sahibi="",Bakiye=0):
        self.Hesap_Sahibi = Hesap_Sahibi
        self.Bakiye = Bakiye

    def Para_Yatir(self,Miktar):
        self.Bakiye += Miktar
        return f"Hesabiniza {Miktar}TL yuklendi\nYeni bakiyeniz: {self.Bakiye}TL"

    def Para_Cek(self,Miktar):
        if self.Bakiye >= Miktar:
            self.Bakiye -= Miktar
            return f"Hesabinizdan {Miktar}TL cekildi\nYeni bakiyeniz: {self.Bakiye}TL"
        else:
            return f"Yetersiz bakiye!"

    def Bilgi_ver(self):
        return f"{self.Hesap_Sahibi} bakiyen: {self.Bakiye}TL"

Hesap_1 = Banka_Hesabi("John",2000)
print(Hesap_1.Para_Yatir(500))
print(Hesap_1.Para_Cek(750))
print(Hesap_1.Bilgi_ver())