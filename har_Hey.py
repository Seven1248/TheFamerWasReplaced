#種植並收閤牧草
def run():
	size = get_world_size()
	for h in range(size):
		for i in range(size):	
			harvest()
			move(North)
		move(East)

if __name__ == "__main__":
	run()	