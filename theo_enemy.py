from weapon_theo import *
class enemy:
    def get_attack(self):
        return "slash"

    def take_damage(self, damage):
        self.hp = self.hp - damage

class dragon(enemy):
    def __init__(self):
        self.hp = 150
        self.weapon = dagger()
        self.abilities = "can breathe fire and dodge attacks by flying out of the way."
    def __repr__(self):
        return "dragon"
        
class skeleton(enemy):
    def __init__(self):
        self.hp = 140
        self.weapon = "bow_and_arrow"
        self.abilities = "can come apart and come together again in a different spot."
    def __repr__(self):
        return "skeleton" 

class zombie(enemy):
    def __init__(self):
        self.hp = 300
        self.weapon = "spikey_club"
        self.abilities = "needs to be killed multiple times to really be dead."
    def __repr__(self):
        return "zombie"        
