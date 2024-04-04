import random
import numpy as np

class Boss:
    def __init__(self, p_basic, p_stun):
        self.HP = 30
        self.p_basic = p_basic
        self.p_stun = p_stun

    def choose_attack(self):
        return np.random.choice(3, 1, p=[0, self.p_basic, self.p_stun])[0]
    

    def deal_basic_dmg(self):
        return random.randint(2,7), False
    
    def deal_stun_dmg(self):
        return 1, True
    
    def deal_dmg(self):
        attack = self.choose_attack()
        if(attack == 1):
            return self.deal_basic_dmg(), attack
        elif(attack == 2):
            return self.deal_stun_dmg(), attack

    def take_dmg(self, player):
        dmg = player.deal_dmg()
        self.HP -= dmg

    def getProbs(self):
        return self.p_basic, self.p_stun

    def dead(self):
        return self.HP <= 0

    def __str__(self):
        return str(self.HP)