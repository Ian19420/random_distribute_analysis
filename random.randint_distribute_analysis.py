import random
#取範圍1~10是否為平均分佈 
list_num = [random.randint(1,10) for _ in range(10000)]
dict_num = {n: list_num.count(n) for n in set(list_num)}
for i in sorted(dict_num.keys()):
	print(f"{i}有{dict_num[i]}個")

