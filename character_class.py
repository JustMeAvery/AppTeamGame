from theo_armor import *
from weapon_theo import *

xp_req_by_lvl = {	1:0,
				 	2:100,
				 	3:500,
				 	4:__
				 	}

class character():
	def __init__(self, name, species):
		self.maxhp = 500
		self.hp = 500
		self.inventory = []
		self.name = name
		self.weapon = dagger()
		self.species = species
		self.helm = None
		self.chest_armor = None
		self.leg_armor = None
		self.shield = shield()
		self.xp = 0
		self.level = 1

	def __repr__(self):
		return self.name + ", the " + self.species

	def levelup(self):
		# TODO: fill this in with a check whether you should level up then do it if the check is True
		pass


	def cba(self):
		if self.helm and self.helm.dur == 0:
			self.helm = None
		if self.chest_armor and self.chest_armor.dur == 0:
			self.chest_armor = None
		if self.leg_armor and self.leg_armor.dur == 0:
			self.leg_armor = None
		if self.shield and self.shield.dur == 0:
			self.shield = None
		

	def take_damage(self, damage):
		while damage > 0:
			armor_pieces = [armor for armor in [self.helm, self.chest_armor, self.leg_armor, self.shield] if armor != None]		
			num_armor = len(armor_pieces)
			split_dmg = damage/num_armor
			for armor in armor_pieces:
				if armor.dur >= split_dmg:
					armor.dur -= split_dmg
					damage -= split_dmg
				else:
					damage -= armor.dur
					armor.dur = 0
			self.cba()
	

	def get_attack(self):
		while True:
			attack = input("How would U like 2 attack UR enemy? Stab, slash, or crush? [type either 'slash', 'stab', or 'crush']\n")
			if not attack in ["slash", "stab", "crush"]:
				print ("brosseff that was not a valid ansuh")
			else:
				return attack


def new_game():
	while True:
		name = input("Enter your name.\n")
		response = input("Is " + name + " your name? (Type 'y' or 'n' only.)\n")
		if response.lower() == "y":
			species = input("What species of living thing R U?\n")
			response = input("So U R A " + species + "?\n")
			if response.lower() == "y":
				return character(name, species)
