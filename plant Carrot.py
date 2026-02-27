while True:
	for h in range(get_world_size()):
		for i in range(get_world_size()):
			if can_harvest():
				harvest()
				if i == 2:
					till()
					plant(Entities.Carrot)
				else:			
					plant(Entities.Bush)
				move(North)
				
			else:
				move(North)
		
				
		move(East)