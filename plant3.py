clear() #清理環境整地
for h in range(get_world_size()):
	for i in range(get_world_size()):
		if h <= 2 and i <= 2: #在3*3格子內種植南瓜
			till()
			plant(Entities.Pumpkin)
		elif h > 2 and i < 3:
			pass
		elif (i % 2 == 0 and h % 2 ==0) or (i % 2 == 1 and h % 2 ==1) : #在偶數行種植蘿蔔
			plant(Entities.Tree)
		else:
			till()
			plant(Entities.Carrot)
		move(North)
	move(East)
while True:
	for h in range(get_world_size()):
		for i in range(get_world_size()):
			harvest()
			if h <= 2 and i <= 2: #在3*3格子內種植南瓜
				plant(Entities.Pumpkin)
			elif h > 2 and i < 3:
				pass
			elif (i % 2 == 0 and h % 2 ==0) or (i % 2 == 1 and h % 2 ==1) : #在偶數行種植蘿蔔
				plant(Entities.Tree)
			else:
				plant(Entities.Carrot)
			move(North)
		move(East)
		