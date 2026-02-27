while True:
	if can_harvest():
		harvest()
		#plant(Entities.Bush)
	else:
		move(North)
