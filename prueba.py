from os import system

system("cls")

from random import randrange


class Pirate:
    boat_life = 200

    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self, enemy):
        if self.weapon.scope == "short" and enemy.position == "far":
            print("No puedes atacar con ese arma desde esa posicion!")
            return "Attack!!"
        else:
            enemy.health -= self.weapon.damage

    @classmethod
    def hit(cls, damage):
        cls.boat_life -= damage


class Enemy:

    def __init__(self, name, health, position, min_damage, max_damage):
        self.name = name
        self.health = health
        self.position = position
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self, pirate):
        damage = randrange(self.min_damage, self.max_damage)
        Pirate.boat_life -= damage
        print(f"¡Oh no! {self.name} ha atacado a {pirate.name}")

    def move(self):
        if self.position == "far":
            self.position = "near"
        elif self.position == "near":
            self.position = "far"

    def hit(self, damage):
        self.health -= damage


class Weapon:
    def __init__(self, name, damage, scope):
        self.name = name
        self.damage = damage
        self.scope = scope


sword = Weapon("Espada", 3, "short")
ax = Weapon("Hacha", 5, "short")
bow = Weapon("Arco", 2, "short")

torvellino1 = Enemy(
    "Torvellino 1", health=25, position="near", min_damage=2, max_damage=5
)
torvellino2 = Enemy(
    "Torvellino 2", health=25, position="near", min_damage=4, max_damage=8
)
torvellino3 = Enemy(
    "Torvellino 3", health=25, position="far", min_damage=3, max_damage=5
)

torvellino4 = Enemy(
    "Torvellino 4", health=25, position="far", min_damage=6, max_damage=9
)

pyratilla = Pirate("Pyratilla", sword)
pym = Pirate("Pym", bow)
pyerce = Pirate("Pyerce", ax)

pyrates = [pyratilla, pym, pyerce]
enemies = [torvellino1, torvellino2, torvellino3, torvellino4]


def restart_battle():
    print("los enemigos ganan!!")
    enemies = [torvellino1, torvellino2, torvellino3, torvellino4]
    for e in enemies:
        e.health = 25
    Pirate.boat_life = 200
    batalla()


def batalla():
    print("Comienza la batalla!!")

    while len(enemies) > 0:
        print(Pirate.boat_life)
        print(f"Quedan {len(enemies)} enemigos")
        if Pirate.boat_life < 1:
            print("Reiniciamos, los pyrates han perdido")
            restart_battle()

        for pyrate in pyrates:
            if enemies[0].health < 1:
                enemies.remove(enemies[0])
                print("Enemigo muerto")
            if len(enemies) == 0:
                print("La victoria es de los Pyrates!!!")
                break
            else:
                enemyTarget = enemies[0]
                print("salud", enemyTarget.health)
                pyrate.attack(enemyTarget)

        for enemy in enemies:
            al = randrange(0, 2)
            if al == 1:
                enemy.move()
            else:
                pyrateTarget = pyrates[randrange(0, len(pyrates))]
                enemy.attack(pyrateTarget)


batalla()
