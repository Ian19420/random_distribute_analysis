import random 
list_num = [random.randint(1,10) for _ in range(10000)]
dict_num = {n: list_num.count(n) for n in list_num}
for i in dict_num.keys():
	print(f"{i}有{dict_num[i]}個")

