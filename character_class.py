class character():
	def __init__(self, name, species, armor):
		self.hp = 500
		self.items = ""
		self.name = name
		self.weapon = "hi"
		self.species = species
		self.armor = armor


theo = character("theo", "human", "breastplate, helm, and helmet")
print (theo.name)
print (theo.weapon)
print (theo.species)
print (theo.armor)
      
