#import goto_Soil
#goto_Soil.run()
# 設定區域大小
#副程式 檢查仙人掌大小，並與周圍比較，若南比北大則交換；若西比東大則交換；以此類推，直到排序完成為止
def checkAndSwap(CanHar):
	size = get_world_size()
	x = get_pos_x()
	y = get_pos_y()
	current = measure()				
	east_value = measure(East) #確認東邊仙人掌的大小
	west_value = measure(West) #確認西邊仙人掌的大小
	north_value = measure(North)#確認北邊仙人掌的大小
	south_value = measure(South)#確認南邊仙人掌的大小				
	
	CheckPoint1 = False
	while CheckPoint1 == False:#檢查東西方
		CheckPoint1 = True
		if current < west_value and x > 0:#如果西方的值較大則交換
			swap(West)
			current = measure()		
			west_value = measure(West)
			CheckPoint1 = False
			CanHar =False
		if east_value < current and x < size - 1:#如果東方的值較小則交換
			swap(East)
			current = measure()		
			east_value = measure(East)
			CheckPoint1 = False
			CanHar =False
				#quick_print("仙人掌大小為",current,"，X為", x ,"，Y為" ,y,"，世界大小為",size)		
		CheckPoint2 = False
		while CheckPoint2 == False:#檢查南北
			CheckPoint2 = True
			if current < south_value and y > 0:#如果南方的值較大則交換
				swap(South)
				current = measure()		
				south_value = measure(South)
				CheckPoint2 = False
				CanHar =False
			if north_value < current and y < size - 1:#如果北方的值較小則交換
				swap(North)
				current = measure()		
				north_value = measure(North)
				CheckPoint2 = False
				CanHar =False
				#quick_print("仙人掌大小為",current,"，X為", x ,"，Y為" ,y,"，世界大小為",size)
		return CanHar 
def run():
	#測試參數開始，完成時刪除
	#set_world_size(8)
	x = get_pos_x()
	y = get_pos_y()
	for h in range(x):
		move(West)
	for h in range(y):
		move(South) 
	#測試參數結束，完成時刪除

	size = get_world_size()
	# Step 1 種滿仙人掌
	for y in range(size):
		for x in range(size):
			harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Cactus)
			move(East)
		#回到下一行起點
		move(North)
		#回到最西側
	# Step 2 等待成熟
	# 仙人掌固定 1s，可簡單延遲或巡邏等待
	# Step 3 排序
	# 從左下往右上推大數
	CanHar = False #是否可以收成，若無交換則為True
	while CanHar == False:
		CanHar = True
		for y in range(size):
			for x in range(size):
				CanHar = checkAndSwap(CanHar)				
				move(East)
			#回到下一行			
			move(North)
			#反向執行
			if CanHar == False:
				revy = size - 2 - y * 2
				for i in range(abs(revy)):
					if revy > 0:
						move(North)		
					else:
						move(South)		
				for x in range(size):
						move(West)	
						checkAndSwap(False)					
				for i in range(abs(revy)):
					if revy > 0:
						move(South)		
					else:
						move(North)				
			#回到下一行
			#回到最西側
		#print(repeat)
	harvest()
if __name__ == "__main__":
	run()				