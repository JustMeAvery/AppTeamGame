class enemy:

class dragon(enemy):
    def __init__(self):
        self.hp = 500
        self.weapon = "dagger"
        self.abilities = "can breathe fire and dodge attacks by flying out of the way."
        self.attack = raw_input
        
class skeleton(enemy):
    def __init__(self):
        self.hp = 450
        self.weapon = "bow_and_arrow"
        self.abilities = "can come apart and come together again in a different spot."
        
class zombie(enemy):
    def __init__(self):
        self.hp = 1000
        self.weapon = "spikey_club"
        self.abilities = "needs to be killed multiple times to really be dead."
        
