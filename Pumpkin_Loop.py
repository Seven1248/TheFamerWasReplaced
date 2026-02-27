clear()
for h in range(get_world_size()):
		for i in range(get_world_size()):
			harvest()			
			if h <=5 and i <=5 :
				till()
				plant(Entities.Pumpkin)#種植南瓜
			else:
				pass
				#隨機種植
			move(North)
		move(East)
while True:
	for h in range(get_world_size()):
		for i in range(get_world_size()):
			
			if h <=5 and i <=5 :
				plant(Entities.Pumpkin)#種植南瓜
			else:
				harvest()
			move(North)
		move(East)
	CanHar = 0
	CheckPumpkin = 0
	while CanHar == 0 : #檢查南瓜是否收成
		
		for h in range(get_world_size()):
			for i in range(get_world_size()):
				if h <=5 and i <=5 :
					if not(can_harvest()):						
						plant(Entities.Pumpkin)#種植南瓜
						use_item(Items.Fertilizer) #施肥
						CheckPumpkin = CheckPumpkin + 1 #屬鼠壞南瓜
				else:
					harvest()
				move(North)				
			move(East)	
		if CheckPumpkin == 0 :
			CanHar = 1			
			harvest()
		else:
			CheckPumpkin = 0
	
	