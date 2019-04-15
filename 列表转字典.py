# #列表转字典

#将单一列表转换为字典
def lc1(list1,dict1):
    """将list1中的0,2,4...作为键;1,3,5...作为值;
    dict1为转换后的输出
    """
    count = 0
    list2 = []
    if len(list1) %2 == 1:      #判断键值对是否平衡
        print('抱歉，列表中的键值对不平衡，请再输入一个元素,否则将会忽略最后一个元素')

    for i in list1:
        count += 1
        if count == 2:
            count = 0
            list2.append(i)
            dict1.update({list2[0]:list2[1]})
            list2.clear()       #添加完毕，清空列表
        else:
            list2.append(i)
    return dict1


#将两个字典转换为字典
def lc2(list1,list2,dict1):
    """将list1中的每个元素作为键;将list2的每个元素作为值;
    dict1为转换后的输出
    """
    # dict1 = {}
    count = 0
    if len(list1) != len(list2):    #判断键值对是否平衡
        print('你输入的两个列表元素数量不匹配,请修改')
        return

    for i in list1:
        dict1.update({list1[count]:list2[count]})
        count += 1
    return dict1


