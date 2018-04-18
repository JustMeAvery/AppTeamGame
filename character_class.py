from theo_armor import *
from weapon_theo import *
class character():
	def __init__(self, name, species):
		self.hp = 500
		self.inventory = []
		self.name = name
		self.weapon = dagger()
		self.species = species
		self.helm = None
		self.chest_armor = None
		self.leg_armor = None
		self.shield = shield()

	def take_damage(self, damage):
		num_armor = sum([armor != None for armor in [self.helm, self.chest_armor, self.leg_armor, self.shield]])
		#TODO

def new_game():
	name = input("Enter your name.\n")
	response = input("Is " + name + " your name? (Type 'y' or 'n' only.)\n")
	if response.lower() == "y":
		species = input("What species of living thing R U?\n")
		response = input("So U R A " + species + "?\n")
		if response.lower() == "y":
			return character(name, species)
