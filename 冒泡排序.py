# 冒泡排序

def paixu(li1):
    """
    :param li1: 这个是传入的列表
    :return: 返回排序后列表
    """
    print(li1)
    count1 = len(li1)
    count4 = 0  # 记录次数
    # li1 = [1,5,2,7,3,6]
    # 1--5   2--4    3--3    4--2    5--1
    for i in range(count1 - 1):  # 3 -->486 861 61
        count2 = 0
        count3 = count1 - (i + 1)
        for i1 in range(count3):
            count2 += 1
            count4 += 1
            if li1[-count2] < li1[(-count2) - 1]:
                li1[-count2], li1[-count2 - 1] = li1[-count2 - 1], li1[-count2]
            print(li1, count4)
    return li1


li1 = [1, 5, 2, 7, 3, 6]
li2 = []
paixu(li1)
