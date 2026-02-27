def BkToStart():
	#回到原點
	x = get_pos_x()
	y = get_pos_y()
	for h in range(x):
		move(West)
	for h in range(y):
		move(South)
	#回到原點結束
def run():
	size = get_world_size() #取得世界大小
	for h in range(6):
		for i in range(6):
			#DO
			harvest()
			plant(Entities.Pumpkin)
			move(North)			
		for i in range(6):
			move(South) #回去
		move(East)	
	for h in range(6):
		move(West)#回去
	#檢查程式
	Check_Pum = [] #檢查換南瓜
	#quick_print(Check_Pum)	
	#第一次全檢
	for h in range(6):
		for i in range(6):
			#DO
			if not (can_harvest()):
				plant(Entities.Pumpkin)
				Check_Pum.append([get_pos_x(),get_pos_y()]) #加入不良南瓜座標				
			move(North)			
		for i in range(6):
			move(South) #回去
		move(East)
	for h in range(6):
		move(West)#回去	
	#再次檢查	
	while Check_Pum:	#當Check_Pum不為空(有壞南瓜時)
		x, y = Check_Pum.pop(0)   # 取出第一個壞南瓜的座標
		dx = x - get_pos_x()	#計算與壞南瓜的距離
		dy = y - get_pos_y()	
		while dx != 0:			#移動到壞南瓜的x座標
			if dx > 0:
				move(East)
				dx -= 1
			else:
				move(West)
				dx += 1

		while dy != 0:			#移動到壞南瓜的y座標
			if dy > 0:
				move(North)
				dy -= 1
			else:
				move(South)
				dy += 1

		if not can_harvest():  #如果還是不能收成，重新種植並加入檢查列表
			plant(Entities.Pumpkin)
			Check_Pum.append([get_pos_x(), get_pos_y()])
	# while Check_Pum != []:
	# 	#for i in range(len(Check_Pum)):			
	# 		#quick_print(Check_Pum[badPum])
	# 		#quick_print("現在x值是",Check_Pum[i][0],"現在y值是",Check_Pum[i][1])
	# 	for x, y in Check_Pum:
	# 		quick_print("現在x值是", x,"，現在y值是", y)	
	# 		nx = x - get_pos_x()
	# 		ny = y - get_pos_y()
	# 		quick_print("現在和壞南瓜的距離x值是", nx,"，現在和壞南瓜的距離y值是", ny)
	# 		while abs(nx) > 0 :
	# 			if nx > 0 :
	# 				move(East)
	# 				nx -= 1
	# 			else:
	# 				move(West)
	# 				nx +=1				
	# 		while abs(ny) > 0 :
	# 			if ny > 0 :
	# 				move(North)
	# 				ny -= 1
	# 			else :
	# 				move(South)
	# 				ny += 1		
			
	# 		if can_harvest():		#如果能收成，移除不良座標
	# 			Check_Pum.pop(0)
	# 			quick_print(Check_Pum)
	# 		else:
	# 			plant(Entities.Pumpkin)
	# 			Check_Pum.append([get_pos_x(),get_pos_y()])
		#do_a_flip()
	#確認能夠收成，開始收成
	harvest()	
#回到原點
	BkToStart()
#回到原點結束
			
	
	
		
if __name__ == "__main__":
	run()	