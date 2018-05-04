from character_class import *
from theo_enemy import*
attack_type_multipliers = {"stab": 0.75, "slash": 1.0, "crush": 1.5}


def battle_loop(player, enemy):
	# battle info
	# TODO: add context to the prints
	print("You see a(n) " + str(enemy))
	print("It has " + str(enemy.hp) + " health")
	print("Its weapon is a(n) " + str(enemy.weapon))

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
		if turn == 0:
			print("You hit the "+ str(participants[1 - turn])+ " with "+ str(damage) + " damage")
			print("It has " + str(participants[1-turn].hp) + " health remaining. ")
		else:
			print("The "+ str(participants[turn])+ " hits you with "+ str(damage) + " damage")
			print("You have " + str(participants[1-turn].hp) + " health remaining. ")
		turn = 1 - turn
	if enemy.hp <= 0:
		print("You defeated the " + str(enemy) + "! Well done.")
		player.xp += player.hp
		player.levelup()
		player.hp = player.maxhp
		return True

	else:
		print("You were defeated by the " + str(enemy) + ". Better luck next time!")
		return False	

# TODO: write order of battles for game

p = new_game()
e = dragon()
e.hp = 10
battle_loop(p,e)
