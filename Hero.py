class hero :
    def __init__ (self, nama, darah, serangan, senjata, role):
        self.nama = nama
        self.darah = darah
        self.serangan = serangan
        self.role = role
        self.senjata = senjata

    def introduce(self):
        return f"{self.nama} adalah hero dengan darah: {self.darah} hp, {self.serangan} attack, dengan role {self.role} dengan senjata {self.senjata} "

    def special_ability(self):
        pass

class Asassin(hero):
    def __init__(self, nama):
        super().__init__(nama, darah=10000, serangan=5000, senjata="Tombak sakti legendaris pemikat janda dunia ke 3", role="Asassin")

    def special_ability(self):
        return f"{ self.nama} menggunakan kemampuan: gesit - damage tinggi"

Asassin_hero = Asassin("Zilong")

print(Asassin_hero.introduce())
print(Asassin_hero.special_ability())
     