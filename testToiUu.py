def sort_dict(x, dic):
    temp_dic = dict()
    for i in dic.keys():
        if dic.get(i) <= x:
            temp_dic[i] = dic.get(i)
    dicA = dict(sorted(temp_dic.items(),
                       key=lambda value: value[1], reverse=True))
    temp_dic.clear()
    return dicA


def max_dict(x, dic):
    max_dic = dict()
    temp_dic = sort_dict(x, dic)
    for i in temp_dic.keys():
        if x - temp_dic.get(i) >= 0:
            max_dic[i] = temp_dic.get(i)
            temp_dic.clear()
        break
    # if len(max_dic.keys()) == 0:
    # 	return max_dic = max_dic['0'] == 0
    return max_dic


def first_vale_dic(dic):
    a = int()
    for key in dic.keys():
        a = dic.get(key)
        break
    return a


def first_key_dic(dic):
    a = int()
    if len(dic.keys()) != 0:
        for key in dic.keys():
            a = key
            break
        return a
    a == 0
    return a


dic = {'1': 2, '2': 2, '3': 3, '4': 4, '5': 5, '6': 3, '7': 6, '8': 7, '9': 10}
x = 1
# def lst_key_ketQua(x, dic):
lst_dic_kq = list()
c = x
ls_temp_dic = dict()
# for i in dic.keys():
#     ls_temp_dic[i] = dic.get(i)

while c != 0 or len(sort_dict(c, dic).keys()) != 0:
    i = first_key_dic(max_dict(c, sort_dict(c, dic)))
    if i is None or i == 0:
        lst_dic_kq.append(0)
        break
    else:
        lst_dic_kq.append(i)
        c = c - first_vale_dic(max_dict(c, sort_dict(c, dic)))
        del dic[i]
# return lst_dic_kq


print(lst_dic_kq)

# 10,7,6,2

# 9: 10   25 --> i = '9', c =25 - 10 = 15
# 8: 7
# 7: 6
# 4: 4
# 3: 3
# 6: 3
# 2: 2
# 5: 2
# 1: 1
