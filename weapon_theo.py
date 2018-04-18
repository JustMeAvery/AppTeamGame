class weapon():
	def get_attack(self):
		return self.damage

class sword(weapon):
	def __init__(self):
		self.damage = 5
		self.durability = 50
		self.speed = 6
		self.dtype = "TBD"

class dagger(sword):
	def __init__(self):
		self.damage = 5
		self.durability = 50
		self.speed = 7
		self.dtype = "stab"
		
		
class rusty_dagger(dagger):
	def __init__(self):
		self.damage = 10
		self.durability = 60
		self.speed = 6.5
		self.dtype = "stab and infect wound (enemies die faster)"
	
		
		
		
class poisoned_dagger(dagger):
	def __init__(self):
		self.damage = 15
		self.durability = 70
		self.speed = 6
		self.dtype = "stab and poison enemy wound (enemies die even faster)"
		
		
		
class medieval_sword(sword):
	def __init__(self):
		self.damage = 20
		self.durability = 70
		self.speed = 6
		self.dtype = "cut"

class rusty_medieval_sword(medieval_sword):
	def __init__(self):
		self.damage = 25
		self.durability = 80
		self.speed = 5.5
		self.dtype = "cut and infect wound (enemies die faster)"

class poisoned_medieval_sword(medieval_sword):
	def __init__(self):
		self.damage = 30
		self.durability = 90
		self.speed = 5
		self.dtype = "cut and poison (enemies even die faster)"



class club(weapon):
	def __init__(self):
		self.damage = 5
		self.durability = 50
		self.speed = 6
		self.dtype = "TBD"

class wooden_club(club):
	def __init__(self):
		self.damage = 5
		self.durbaility = 50
		self.speed = 7
		self.dtype = "whack and temporarily stun the enemy/ies"
		
class spiky_wooden_club(club):
	def __init__(self):
		self.damage = 10
		self.durability = 60
		self.speed = 6.5
		self.dtype = "whack, wound, and temporarily stun the enemy/ies"

class spiky_poisoned_wooden_club(club):
	def __init__(self):
		self.damage = 15
		self.durability = 70
		self.speed = 6
		self.dtype = "whack, wound, poison the wound, and temporarily stun the enemy/ies (they die fster with the poison)"
		
class metal_club(club):
	def __init__(self):
		self.damage = 20
		self.durability = 70
		self.speed = 6
		self.dtype = "whack and temporarily stun the enemy/ies (longer than the wooden club)"
		
class spiky_metal_club(metal_club):
	def __init__(self):
		self.damage = 25
		self.durability = 80
		self.speed = 5.5
		self.dtype = "whack, wound, and temporarily stunt the enemy/ies (longer than the wooden club)"
		
class spiky_poisoned_metal_club(metal_club):
	def __init__(self):
		self.damage = 30
		self.durability = 90
		self.speed = 5
		self.dtype = "whack, wound, poison the wound, and temporarily stunt the enemy/ies (longer than the wodden club)"


class blaster(weapon):
	def __init__(self):
		self.damage = 5
		self.durability = 50
		self.speed = 6
		self.dtype = "TBD"
		
class average_blaster(blaster):
	def __init__(self):
		self.damage = 5
		self.durability = 50
		self.speed = 7
		self.dtype = "blasts and temorarily stuns enemies"

class supa_average_blaster(average_blaster):
	def __init__(self):
		self.damage = 10
		self.durability = 60
		self.speed = 6.5
		self.dtype = "blasts and temorarily stuns enemies"

class supa_mega_average_blaster(average_blaster):
	def __init__(self):
		self.damage = 15
		self.durability = 70
		self.speed = 6
		self.dtype = "blasts and temorarily stuns enemies"

class awesome_blaster(blaster):
	def __init__(self):
		self.damage = 20
		self.durability = 70
		self.speed = 6
		self.dtype = "blasts and temorarily stuns enemies (for longer than the average blaster)"

class supa_awesome_blaster(awesome_blaster):
	def __init__(self):
		self.damage = 25
		self.durability = 80
		self.speed = 5.5
		self.dtype = "blasts and temorarily stuns enemies (for longer than the average blaster)"
	
class supa_mega_awesome_blaster(awesome_blaster):
	def __init__(self):
		self.damage = 30
		self.durability = 90
		self.speed = 5
		self.dtype = "blasts and temporarily stuns enemies (for longer than the average blaster)"


		
		
class bow_and_arrow(weapon):
	def __init__(self):
		self.damage = 5
		self.durability = 50
		self.speed = 6
		self.dtype = "whatever the bows do"
		
class average_bow_and_sharp_arrow(bow_and_arrow):
	def __init__(self):
		self.damage = 5
		self.durability = 50
		self.speed = 7
		self.dytpe = "whatever the bows do"
		
class supa_average_bow_and_supa_sharp_arrow(average_bow_and_sharp_arrow):
	def __init__(self):
		self.damage = 10
		self.durability = 60
		self.speed = 6.5
		self.dtype = "whatever the bows do"
		
class supa_mega_average_bow_and_supa_mega_sharp_arrow(average_bow_and_sharp_arrow):
	def __init__(self):
		self.damage = 15
		self.durability = 70
		self.speed = 6
		self.dtype = "whatever the bows do"
		
class awesome_bow_and_poisoned_arrow(bow_and_arrow):
	def __init__(self):
		self.damage = 20
		self.durability = 70
		self.speed = 6
		self.dtype = "whatever the bows do only better and poisonous"
		
class supa_awesome_bow_and_supa_poisoned_arrow(awesome_bow_and_poisoned_arrow):
	def __init__(self):
		self.damage = 25
		self.durability = 80
		self.speed = 5.5
		self.dtype = "whatever the bows do only better and poisonous"
		
class supa_mega_awesome_bow_and_supa_mega_awesome_poisoned_arrow(awesome_bow_and_poisoned_arrow):
	def __init__(self):
		self.damage = 30
		self.durability = 90
		self.speed = 5
		self.dtype = "whatever the bows do only better and poisonous"
		

#what the heck how do i write test code kevin?????!!!!!!!!!


w = supa_mega_awesome_bow_and_supa_mega_awesome_poisoned_arrow()
print(w.damage)
print(w.speed)
print(w.durability)
print(w.dtype)














































