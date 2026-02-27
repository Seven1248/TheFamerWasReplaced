#import goto_Soil
#goto_Soil.run()
# 設定區域大小
def run():
	size = get_world_size()
	# Step 1 種滿仙人掌
	for y in range(size):
		for x in range(size):
			harvest()
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
				current = measure()						
				east_value = measure(East) #確認東邊的值
				west_value = measure(West) #確認東邊的值
				north_value = measure(North)#確認北邊的值
				south_value = measure(South)#確認南邊的值				
				if x < size -1 : #當x不在最東邊
					CheckPoint1 = False
					while CheckPoint1 == False:#檢查東西方
						CheckPoint1 = True
						if current < west_value and x > 0:#如果西方的值較大則交換
							swap(West)
							current = measure()		
							west_value = measure(West)
							CheckPoint1 = False
							CanHar = False
						if east_value < current :#如果東方的值較小則交換
							swap(East)
							current = measure()		
							east_value = measure(East)
							CheckPoint1 = False
							CanHar = False
						#quick_print("仙人掌大小為",current,"，X為", x ,"，Y為" ,y,"，世界大小為",size)				
				if   y < size - 1:# 當y值不在最北邊
					CheckPoint2 = False
					while CheckPoint2 == False:#檢查南北
						CheckPoint2 = True
						if current < south_value and y > 0:#如果南方的值較大則交換
							swap(South)
							current = measure()		
							south_value = measure(South)
							CheckPoint2 = False
							CanHar = False
						if north_value < current :#如果北方的值較小則交換
							swap(North)
							current = measure()		
							north_value = measure(North)
							CheckPoint2 = False
							CanHar = False
						#quick_print("仙人掌大小為",current,"，X為", x ,"，Y為" ,y,"，世界大小為",size)					
				move(East)
			#回到下一行
			move(North)
			#回到最西側
		#print(repeat)
	harvest()
if __name__ == "__main__":
	run()				