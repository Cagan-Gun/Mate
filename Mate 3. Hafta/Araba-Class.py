class Araba:
    def __init__(self,Marka,Model,Yil):
        self.Marka = Marka
        self.Model = Model
        self.Yil = Yil

    def Bilgi_ver(self):
        return f"Marka: {self.Marka}, Model: {self.Model}, Yil: {self.Yil}"

Araba_1 = Araba("Toyota","Corolla","1966")
Araba_2 = Araba("Renault","Clio","1990")
print(f"Birinci arabanin bilgileri:\n{Araba_1.Bilgi_ver()}")
print(f"İkinci arabanin bilgileri:\n{Araba_2.Bilgi_ver()}")