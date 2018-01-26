class enemey():
	base_hp=200

class skeleton(enemey):
	def __init__(self):
		self.hp=enemey.base_hp-100
		self.weapon=crossbow()
class zombie(enemey):
	def __init__(self):
		self.hp=enemey.base_hp-50
		self.weapon=club()
class dragon(enemey):
	def __init__(self):
		self.hp=enemey.base_hp+150
		self.weapon=fire()
class goblin(enemey):
	def __init__(self):
		self.hp=enemey.base_hp-100
		self.weapon=sword()
class kieran(enemey):
	def __init__(self):
		self.hp=enemey.base_hp+300
		self.weapon=bazooka()
