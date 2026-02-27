#將草地整理為農地
def run():
	size = get_world_size()
	
	x = get_pos_x()
	y = get_pos_y()
	for h in range(size):
			for i in range(size):
				harvest()
				GroundTypes	= get_ground_type() 
				while GroundTypes == Grounds.Grassland:
					till()
					GroundTypes	= get_ground_type()								
				move(North)
			move(East)
	for h in range(x):
		move(West)
	for h in range(y):
		move(South)
if __name__ == "__main__":
	run()


