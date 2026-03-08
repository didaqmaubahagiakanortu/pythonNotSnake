from abc import ABC, abstractmethod

class GameUnit(ABC):

    @abstractmethod
    def serang(self, lawan):
        pass

    @abstractmethod
    def info(self):
        pass

class Hero(GameUnit):
    def __init__(self, name, hp_awal, attack_power):
        self.name = name
        self.__hp = hp_awal
        self.attack_power = attack_power

    def get_hp(self):
        return self.__hp
    
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def info(self):
        print(f"Agent: {self.name} | HP: {self.get_hp()} | Power: {self.attack_power}")

    def serang(self):
        print(f"{self.name} menyerang dengan tangan kosong!")

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.get_hp()}")

class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis
    
    def serang(self, lawan):
        print(f"Monster {self.jenis} menggigit {lawan}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")

class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def serang(self):
        print(f"{self.name} (Mage) menembakkan Bola Api! Boom!")

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.get_hp()} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else: 
            print(f"{self.name} gagal skill! Mana tidak cukup.")

class Archer(Hero):
    def serang(self):
        print(f"{self.name} (Archer) memanah dari jauh! Jeb!")

class Fighter(Hero):
    def serang(self):
        print(f"{self.name} (Fighter) memukul dengan pedang! Slash!")

class Healer(Hero): 
    def serang(self):
        print(f"{self.name} (Healer) tidak menyerang, tetapi menyembuhkan teman!")

print("# Membuat Class Hero\n")

hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

print("\n# Interaksi Antar Objek (Method)")

print("\n--- Pertarungan Dimulai ---\n")
hero1.serang()
hero2.serang()

print("\n# Pewarisan (Inheritance)")

print("\n--- Update Class Hero ---\n")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang()
eudora.skill_fireball(balmond)

print("\n# Enkapsulasi (Mengamankan Data HP)\n")

hero1.set_hp(-50)
print(hero1.get_hp())

print("\nAbstraction & Interface (Membuat Kontrak/Standar)\n")

h = Hero("Alucard", 300, 250)
m = Monster("Serigala")

h.info()
m.info()

print("\nPolymorphism (Fleksibilitas Interaksi)\n")

pasukan = [
    Mage("Eudora", 80, 30, 100),
    Archer("Miya", 90, 100),
    Fighter("Zilong", 100, 30),
    Mage("Gord", 110, 80, 110),
    Healer("Estes", 100, 100)
]

print("--- PERANG DIMULAI ---")

for pahlawan in pasukan:
    pahlawan.serang()