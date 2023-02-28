# MiniProject
# Create a class called Character with the following attributes and methods:
# attribute name
# attribute life – starts with a default value of 20
# attribute attack – the base attack of a character (integer) will be a default of 10
# method basic_attack() - accepts another Character instance as a parameter. Your character will <attack> the other character so his <life> points should drop.

# Now create 3 different classes that inherit from Character:
# Every character type should say (ie. print) something when they are created, get creative :)
# Druid:
# meditate() - increases life by 10, decrease attack by 2
# animal_help()- increases attack by 5
# fight() - accepts another Character instance as a parameter and subtracts (0.75*life + 0.75*attack) from the other character’s life.
# Example:
# druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)
# Warrior:
# brawl() - accepts another Character instance as a parameter, subtracts (2*attack) to the other characters life and adds (0.5*attack) to his own life.
# train() - increases both your attack and life points by 2.
# roar() - accepts another Character instance as a parameter and subtracts their attack points by 3.
# Mage:
# curse() – accepts another Character instance as a parameter and subtracts their attack points by 2.
# summon() - increases attack attribute by 3 points.
# cast_spell() - accepts another Character instance as a parameter and subtracts attack/life to the other character’s life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).
# Once all your classes are created start testing them, create one of each character and use each of their method.


class Character:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10

    def attack_other(self, other):
        other.life -= self.attack
        print(f"{self.name} attacked {other.name} and deal {self.attack} damage")

    def basic_attack(self, other):
        self.attack_other(other)

    def display_status(self):
        print(f"{self.name} ---Life: {self.life} ---Attack {self.attack}")


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} the Druid has been created.")

    def meditate(self):
        self.life += 10
        self.attack -= 2
        print(f"{self.name} meditated and gained 10 life points but lost 2 attack points.")

    def animal_help(self):
        self.attack += 5
        print(f"{self.name} called for animal help and gained 5 attack points.")

    def fight(self, other):
        damage = int(0.75 * self.life + 0.75 * self.attack)
        other.life -= damage
        print(f"{self.name} fought {other.name} and dealt {damage} damage.")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} the Warrior has been created.")

    def brawl(self, other):
        damage = 2 * self.attack
        other.life -= damage
        self.life += int(0.5 * self.attack)
        print(
            f"{self.name} brawled with {other.name}, dealt {damage} damage and gained {int(0.5 * self.attack)} life points.")

    def train(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} trained and gained 2 attack points and 2 life points.")

    def roar(self, other):
        other.attack -= 3
        print(f"{self.name} roared at {other.name} and decreased their attack points by 3.")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name} the Mage has been created.")

    def curse(self, other):
        other.attack -= 2
        print(f"{self.name} cursed {other.name} and decreased their attack points by 2.")

    def summon(self):
        self.attack += 3
        print(f"{self.name} summoned a powerful creature and gained 3 attack points.")

    def cast_spell(self, other):
        damage = int(self.attack / 5) + int(self.life / 10)
        other.life -= damage
        print(f"{self.name} cast a spell on {other.name} and dealt {damage} damage.")


druid = Druid("Conan")
warrior = Warrior("Saber")
mage = Mage("Merlin")

druid.display_status()
warrior.display_status()
mage.display_status()

druid.meditate()
warrior.train()
mage.summon()

druid.fight(warrior)
warrior.roar(mage)
mage.curse(druid)


#
# druid.fight(warrior)
# warrior.brawl(mage)
# mage.cast_spell(druid)
