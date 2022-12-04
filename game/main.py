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
            raise SystemExit

    @staticmethod
    def get_stat(stat):
        while True:
            try:
                return int(input(f"how much points do you want to spend on {stat}?"))
            except ValueError:
                print("must be a whole number")


class Monster:
    monster_names = ['spider', 'moskovyt', 'goblin', 'slime', 'skeleton', 'ghoul', 'werewolf', 'ghost', 'bandit',
                     'viter(super_rare)', 'witch']

    monsters = {}

    def __init__(self, toughness, damage, monster_name, monster_id):
        self.monster_id = monster_id
        self.toughness = toughness
        self.damage = damage
        self.name = monster_name
        self.print_info()

    def print_info(self):
        print(f"{self.monster_id} - {self.name}")
        print(f"toughness - {self.toughness}")
        print(f"damage - {self.damage}")
        print("===============")

    def deal_damage(self):
        return self.damage()

    def be_damaged(self, dealt_damage, monster_id, player):
        self.toughness -= dealt_damage
        if self.toughness <= 0:
            Monster.monsters.pop(monster_id)
            print("you killed this monster")
            player.kills += 1
            player.level_up()

    @classmethod
    def spawn_monsters(cls):
        for i in range(3):
            cls.monsters.update(cls.generate_monster(i))

    @classmethod
    def generate_monster(cls, index):
        new_toughness = r.randint(0, 30)
        new_damage = r.randint(0, 30)
        new_monster_name = cls.generate_name()

        return {
            index: Monster(toughness=new_toughness, damage=new_damage, monster_name=new_monster_name, monster_id=index)
        }

    @classmethod
    def generate_name(cls):
        return cls.monster_names[r.randint(0, len(cls.monster_names) - 1)]
        # monster_names = ['spider', 'moskovyt', 'goblin', 'slime', 'skeleton', 'ghoul', 'werewolf', 'ghost', 'bandit',
        # monster_names[0]

    @staticmethod
    def print_all_info():
        for monster in Monster.monsters.values():
            monster.print_info()


class Game:
    class Fight:
        def __init__(self, player):
            Monster.spawn_monsters()
            self.player = player
            self.battle()

        def damage_phase(self):
            choice = int(input("which monster do you want to fight?"))
            self.player.be_damaged(Monster.monsters[choice].damage)
            Monster.monsters[choice].be_damaged(dealt_damage=self.player.damage, monster_id=choice, player=self.player)

        def battle(self):
            while True:
                self.damage_phase()
                if len(Monster.monsters) == 0:
                    print("you have killed all monsters")
                    break
                Monster.print_all_info()
                self.player.print_info()


if __name__ == "__main__":
    player_1 = Player()
    Game.Fight(player=player_1)
