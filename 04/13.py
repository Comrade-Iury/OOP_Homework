class Weapon:
    def __init__(self, name: str, damage: int, range: int):
        self.name, self.damage, self.range = name, damage, range

    def hit(self, actor, target):
        actor_x, actor_y = actor.get_coords()
        target_x, target_y = target.get_coords()
        if target.is_alive():
            if (abs((actor_x ** 2 + actor_y ** 2) ** 0.5 - (target_x ** 2 + target_y ** 2) ** 0.5)) <= self.range:
                print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
                target.get_damage(self.damage)
            else:
                print(f"Враг слишком далеко для оружия {self.name}")
        else:
            print("Враг уже повержен")

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x, self.pos_y, self.hp = pos_x, pos_y, hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        if self.hp > 0:
            return True
        return False

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon: Weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if type(target) is MainHero:
            self.weapon.hit(self, target)
        else:
            print("Могу ударить только Главного героя")

    def __str__(self):
        return f"Враг на позиции {(self.pos_x, self.pos_y)} с оружием {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.active_weapon = 0

    def hit(self, target: BaseCharacter):
        if self.weapons:
            if type(target) is BaseEnemy:
                self.weapons[self.active_weapon].hit(self, target)
            else:
                print("Могу ударить только Врага")
        else:
            print("Я безоружен")

    def add_weapon(self, weapon):
        if type(weapon) is Weapon:
            self.weapons.append(weapon)
            print(f"Подобрал {weapon.name}")
        else:
            print("Это не оружие")

    def next_weapon(self):
        if self.weapons:
            if len(self.weapons) == 1:
                print("У меня только одно оружие")
            else:
                if self.active_weapon + 1 == len(self.weapons):
                    self.active_weapon = 0
                else:
                    self.active_weapon += 1
                print(f"Сменил оружие на {self.weapons[self.active_weapon].name}")
        else:
            print("Я безоружен")

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f"Полечился, теперь здоровья {self.hp}")
