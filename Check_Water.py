def run():
	size = get_world_size()
	for h in range(size):
		for i in range(size):	
			while get_water() < 0.75 and num_items(Items.Water) != 0 :
				use_item(Items.Water)				
			move(North)
		move(East)
if __name__ == "__main__":
	run()	
