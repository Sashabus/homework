import random as r


class Player:
    def __init__(self):
        self.points = 30
        self.toughness = 0
        self.damage = 0
        self.kills = 0
        self.update_stats()
        self.print_info()

    def update_stats(self):
        print(f"you have {self.points} points, you can spread them between toughness and damage")
        while True:
            delta_toughness = Player.get_stat("toughness")
            delta_damage = Player.get_stat("damage")
            if delta_toughness + delta_damage == self.points:
                self.toughness += delta_toughness
                self.damage += delta_damage
                break
            else:
                print("you had 30 points, you have to spend them all and not a one more!")
        self.points = 0

    def print_info(self):
        print("player stats:")
        print(f"toughness: {self.toughness}")
        print(f"damage: {self.damage}")
        print(f"kills: {self.kills}")

    def level_up(self):
        print("you have leveled up, congrats")
        self.print_info()
        self.points = 30
        self.update_stats()

    def deal_damage(self):
        return self.damage

    def be_damaged(self, dealt_damage):
        self.toughness -= dealt_damage
        if self.toughness <= 0:
            print("game over")
            raise

    @staticmethod
    def get_stat(stat):
        while True:
            try:
                return int(input(f"how much points do you want to spend on {stat}?"))
            except ValueError:
                print("must be a whole number")


class Monster:
    monsters = []


    def __init__(self, toughness, damage, monster_name):
        self.toughness = toughness
        self.damage = damage
        self.print_info(monster_name)

    def print_info(self, num=None):
        if num is not None:
            print(f"monster number {num}:")
        print(f"toughness - {self.toughness}")
        print(f"damage - {self.damage}")

    def deal_damage(self):
        return self.damage()

    def be_damaged(self, dealt_damage, num):
        self.toughness -= dealt_damage
        if self.toughness <= 0:
            Monster.monsters.pop(num)
            print("you killed this monster")
            player_1.kills += 1
            player_1.level_up()

    @classmethod
    def spawn_monsters(cls):
        for i in range(3):
            cls.monsters.append(Monster(toughness=r.randint(0, 30), damage=r.randint(0, 30), monster_name=))

    @staticmethod
    def print_all_info():
        n = 0
        for monster in Monster.monsters:
            print(monster.print_info(n))
            n += 1


while True:
    choice = input("write 'start' to start the game")
    if choice == "start":
        player_1 = Player()
        print("rules")
        while True:
            choice = input("write the command('fight', 'exit')")
            if choice == "fight":
                Monster.spawn_monsters()
                while True:
                    choice = int(input("which monster do you want to fight?"))
                    player_1.be_damaged(Monster.monsters[choice].damage)
                    Monster.monsters[choice].be_damaged(player_1.damage, choice)
                    Monster.print_all_info()
                    player_1.print_info()
                    if len(Monster.monsters) == 0:
                        print("you have killed all monsters")
                        break  # test
