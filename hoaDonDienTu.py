def sort_dict(x, dic):
    temp_dic = dict()
    for i in dic.keys():
        if dic.get(i) <= x:
            temp_dic[i] = dic.get(i)
    dicA = dict(sorted(temp_dic.items(),
                       key=lambda value: value[1], reverse=True))
    temp_dic.clear()
    return dicA


dic = {'1': 2, '2': 2, '3': 3, '4': 4, '5': 2, '6': 3, '7': 6, '8': 7, '9': 10}
x = 1

max_dic = dict()
temp_dic = sort_dict(x, dic)
for i in temp_dic.keys():
    if x - temp_dic.get(i) >= 0:
        max_dic[i] = temp_dic.get(i)
        temp_dic.clear()
    break
if len(max_dic.keys()) == 0:
    return max_dic['0'] = 0
return max_dic
