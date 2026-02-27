def run():
	harvest()
	plant(Entities.Bush)
	substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	directions = [North, East, South, West]
	index = 0
	while get_entity_type() != Entities.Treasure:	
		index = (index - 1) % 4
		if can_move(directions[index]):
			move(directions[index])
		else :
			index = (index + 1) % 4
			if can_move(directions[index]):
				move(directions[index])
			else:
				index = (index + 1) % 4
				if can_move(directions[index]):
					move(directions[index])
				else:
					index = (index + 1) % 4
					move(directions[index])				
	harvest()

if __name__ == "__main__":
	run()
