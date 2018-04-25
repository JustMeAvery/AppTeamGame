from character_class import *
from theo_enemy import*
attack_type_multipliers = {"stab": 0.75, "slash": 1.0, "crush": 1.5}


def battle_loop(player, enemy):
	# battle info
	# TODO: add context to the prints
	print (enemy)
	print (enemy.hp)
	print (enemy.weapon)

	participants = [player, enemy]
	# loop until u win/lose
	turn = 0
	while player.hp > 0 and enemy.hp > 0:
		# get slash, stab, etc
		at = participants[turn].get_attack()
		# calculate damage
		damage = participants[turn].weapon.damage * attack_type_multipliers[at]
		participants[turn].weapon.durability-=5 * attack_type_multipliers[at]
		# deal damage
		participants[1 - turn].take_damage(damage)
		print("The "+participants[turn]+"hits the"+ participants[1 - turn]+ "with "+ damage + "damage")


p = new_game()
e = dragon()
battle_loop(p,e)