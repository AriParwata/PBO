# Class Hero dasar
class Hero:
    def __init__(self, name, health, attack, defense, role):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.role = role

    def introduce(self):
        return f"{self.name} adalah {self.role} dengan {self.health} HP, {self.attack} attack, dan {self.defense} defense."

    def special_ability(self):
        pass  # Method ini akan diimplementasikan di kelas turunan


# Class Assassin (Turunan dari Hero)
class Assassin(Hero):
    def __init__(self, name):
        super().__init__(name, health=1500, attack=300, defense=100, role="Assassin")
    
    def special_ability(self):
        return f"{self.name} menggunakan kemampuan: Serangan Cepat - Damage tinggi pada target lemah."


# Class Mage (Turunan dari Hero)
class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, health=1200, attack=350, defense=80, role="Mage")
    
    def special_ability(self):
        return f"{self.name} menggunakan kemampuan: Ledakan Sihir - Serangan area dengan damage besar."


# Contoh penggunaan class
assassin_hero = Assassin("Fanny")
mage_hero = Mage("Zilong")

# Memperkenalkan karakter dan kemampuan spesial mereka
print(assassin_hero.introduce())
print(assassin_hero.special_ability())

print(mage_hero.introduce())
print(mage_hero.special_ability())
