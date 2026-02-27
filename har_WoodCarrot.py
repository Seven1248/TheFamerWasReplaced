def run(): #種植樹和蘿蔔
	size = get_world_size()
	for h in range(size):
		for i in range(size):
			harvest() #收成前次作物
			if(i % 2 ==0 and h % 2 ==0) or (i % 2 == 1 and h % 2 ==1) :
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Carrot)
			else:				
				plant(Entities.Tree)	
				if num_items(Items.Fertilizer)>0: #如果有肥料就施肥
					use_item(Items.Fertilizer) #施肥			
			move(North)
		move(East)
	#將上個步驟反過來
	for h in range(size):
		for i in range(size):
			harvest() #收成前次作物
			if(i % 2 ==0 and h % 2 ==0) or (i % 2 == 1 and h % 2 ==1) :
				plant(Entities.Tree)
			else:				
				if get_ground_type() == Grounds.Grassland:
					till()
				plant(Entities.Carrot)
			move(North)
		move(East)
if __name__ == "__main__":
	run()