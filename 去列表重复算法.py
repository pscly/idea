
#想写个算法去重
l = [1,2,3,4,5,1,2,3,4,6,1,2,3,7,8,'qwe','qwe','qw']

count1 = len(l)
l_del = []      #即将被删除的空列表
l_del2 = []     #被删除的元素,避免重复删除
for i in l:
    x = 0       #如果进入循环就保存l_del2
    count2 = l.count(i)
    while count2 >= 2 and (i not in l_del2):
        l_del.append(i)
        count2 -= 1
        x += 1
    if x != 0:
        l_del2.append(i)
print(l)
print(l_del)
for i1 in l_del:
    l.remove(i1)
print(l)


# # 失败算法,仅供参考思路
# # a = len(l)
# # while a == 1:
# # 	for i in l:
# # 		for i1 in l:
# # 			if i == i1:
# # 				l.remove(i1)
# # 	a -= 1
# # print(l)
