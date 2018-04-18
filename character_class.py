class character():
	def __init__(self, name, species, armor):
		self.hp = 500
		self.items = ""
		self.name = name
		self.weapon = "dagger"
		self.species = species
		self.armor = armor
		
name = raw_input("What is your character's name?")
species = raw_input("What species of living thing R U?")
print ("Since U R A noob, U will start with this dagger ;). Deal with it.")

theo = character(name, species, "breastplate, helm,")
print (theo.name)
print (theo.weapon)
print (theo.species)
print (theo.armor)

