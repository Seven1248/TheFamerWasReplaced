clear()
while True:
	#種植稻草
	for h in range(get_world_size()):
		for i in range(get_world_size()):
			harvest()
			if get_water() < 0.75 :
				use_item(Items.Water)
			plant(Entities.Bush)#種植灌木叢
			move(North)
		move(East)
	#種植樹和蘿蔔
	for h in range(get_world_size()):
		for i in range(get_world_size()):
			harvest() #收成灌木叢
			if(i % 2 ==0 and h % 2 ==0) or (i % 2 == 1 and h % 2 ==1) :
				till()
				plant(Entities.Carrot)
			else:
				plant(Entities.Tree)
				
			move(North)
		move(East)
	#將上個步驟反過來
	for h in range(get_world_size()):
		for i in range(get_world_size()):
			harvest() #收成灌木叢
			if(i % 2 ==0 and h % 2 ==0) or (i % 2 == 1 and h % 2 ==1) :
				plant(Entities.Tree)
			else:				
				till()
				plant(Entities.Carrot)
			move(North)
		move(East)
	#收穫所有作物並種植南瓜
	for h in range(get_world_size()):
		for i in range(get_world_size()):
			harvest()
			plant(Entities.Pumpkin)#種植南瓜
			move(North)
		move(East)
	CanHar = 0
	CheckPumpkin = 0
	while CanHar == 0 : #檢查南瓜是否收成
		
		for h in range(get_world_size()):
			for i in range(get_world_size()):
				if can_harvest():
					move(North)
				else:
					plant(Entities.Pumpkin)#種植南瓜
					use_item(Items.Fertilizer) #施肥
					CheckPumpkin = CheckPumpkin + 1 #屬鼠壞南瓜
					move(North)
				
			move(East)	
		if CheckPumpkin == 0 :
			CanHar = 1
			
			harvest()
		else:
			CheckPumpkin = 0
	# 種植仙人掌
	size = get_world_size()

	# Step 1 種滿仙人掌
	for h in range(size):
		for i in range(size):
			plant(Entities.Cactus)
			move(North)
			#回到下一行起點		
		move(East)
		#回到最西側
	# Step 2 等待成熟 仙人掌固定 1s，可簡單延遲或巡邏等待
	# Step 3 排序
	# 從左下往右上推大數
	repeat = 1
	while repeat != 0 :   # 多掃幾輪確保排序完成
		repeat = 0
		for h in range(size):
			for i in range(size):
				current = measure() #新增目前的值
				# 比較北邊				
				north_value = measure(North)
				if north_value < current and  ( i != size - 1):
					swap(North)
					quick_print( "X=", h, size)
					repeat +=1
				# 比較東邊				
				east_value = measure(East)
				if east_value< current and  ( h != size - 1):
					swap(East)
					quick_print( "y=" , i, size)
					repeat +=1
				move(North)
			#回到下一行
			move(East)
			#回到最西側
		#print(repeat)
	harvest()
	#整地種草
	for h in range(get_world_size()):
		for i in range(get_world_size()):
			till()
			move(North)
		move(East)
		
	