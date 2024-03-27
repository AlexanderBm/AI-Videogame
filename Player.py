import random

class Player:
    def __init__(self):
        self.HP = 10
        self.stun = False

    def deal_dmg(self):
        if self.stun:
            self.stun = False
            return 0
        return random.randint(10, 20)

    def take_dmg(self, boss):
        dmg, attack = boss.deal_dmg()
        self.HP -= dmg[0]
        self.stun = dmg[1]
        return attack
    
    def getHP(self):
        return self.HP

    def dead(self):
        return self.HP <= 0
        
    def __str__(self):
        return str(self.HP) + " " + str(self.stun)