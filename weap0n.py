class weapon():
	base_damage=0
class bow(weapon):
	def__init__(self):
		self.damage =weapon.base_damage+5
class Sword(weapon):
	def__init__(self):
		self.damage=weapon.base_damage+20
class knife(weapon):
	def__init__(self):
		self.damage=weapon.base_damage+5
class club(weapon):
	def__init__(self):
		self.damage=weapon.base_damage+30

sword=Sword()
print(sword.damage)


class enemy():
	self.hp=100

class skeleton(enemy):
	def __init__(self):
		self.hp= self.hp-50
		self.weapon=bow()

class zombie(enemy):
	def __init__(self):
		self.hp=self.hp
		self.weapon=club()

class dragon(enemy):
	def __init__(self):
		self.hp=self.hp+200
		

class smallG(enemy):
	def __init__(self):
		self.hp=self.hp-25

class bigG(enemy):
	def __init__(self):
		self.hp=self.hp+50
