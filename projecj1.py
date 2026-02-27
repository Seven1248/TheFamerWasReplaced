import goto_Grassland #將農場變更為草地
import har_Hey #種植並收穫稻草
import har_WoodCarrot #種植並收穫木頭與蘿蔔
import UseWeirdSub #汙染農地產生污染物
import goto_Soil #將農場變更為農地
import har_Pumpkin #種植南瓜並收穫
import har_Cactus  #種植排序仙人掌並收穫
import CreatMazes #創建迷宮並完成
import Check_Water #加入澆水程式
while True:
	CreatMazes.run()
	har_Pumpkin.BkToStart()
	har_Hey.run()
	har_WoodCarrot.run()
	UseWeirdSub.run()
	har_Pumpkin.run()
	har_Cactus.run()
	

	