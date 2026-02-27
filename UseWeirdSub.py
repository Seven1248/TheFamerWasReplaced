def run():
#回到原點
	x = get_pos_x()
	y = get_pos_y()
	for h in range(x):
		move(West)
	for h in range(y):
		move(South)
	#建立使用汙染物質的規則
	#對植物使用汙染物質會將四方的植物轉化為汙染物質，反之若對污染植物使用汙染物質則會將四方的污染物質轉化為正常植物
	#程式目標將整個世界由健康植物轉化為汙染物質
	size = get_world_size()
	if num_items(Items.Weird_Substance) <= size * size  * 2:
		for y in range(size):
			for x in range(size):
			#DO
				EntityType = get_entity_type() 
				if x % 5 == 0 and y % 5 == 2:
					use_item(Items.Weird_Substance)
				if x % 5 == 1 and y % 5 == 0:
					use_item(Items.Weird_Substance)
				if x % 5 == 2 and y % 5 == 3:
					use_item(Items.Weird_Substance)
				if x % 5 == 3 and y % 5 == 1:
					use_item(Items.Weird_Substance)
				if x % 5 == 4 and y % 5 == 4:
					use_item(Items.Weird_Substance)
			
			move(East)
		move(North)

if __name__ == "__main__":
	run()