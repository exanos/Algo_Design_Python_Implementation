import random
Men_List=['Abraham','Tyler','Rick','Kyle','Jonathan','John','Nathan','Mike','Mark','Jack','Alex','Mohamed','Ibrahim','Christ','Tony']
Wmn_List=['Ava','Jane','Michele','Mary','Rosanne','Abigail','Amy','Gia','Riley','Evelyn','Charlotte','Mia','Olivia','Eleanor','Aria']
Mprefe={}
Wprefe={}	
for i in Men_List:
	random.shuffle(Wmn_List)
	l=list(Wmn_List)
	Mprefe[i]=l
for i in Wmn_List:
	random.shuffle(Men_List)
	l=list(Men_List)
	Wprefe[i]=l
print('Mprefe:',Mprefe)
print('\n')
print('Wprefe:',Wprefe)

