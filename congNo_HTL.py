# Tạo dicA chứa dữ liệu phải thu.
# Tạo dicB chứa dữ liệu phải trả.
import numpy as np
import pandas as pd
import collections
# -----------------------------------------------------
# Trả về Key của dict , mà có value của key tiệm cần gần nhất với x


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
    for i in dic.keys():
        if x - dic.get(i) >= 0:
            max_dic[i] = dic.get(i)
            dic.clear()
        break
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


def lst_key_ketQua(x, dic):
    lst_dic_kq = list()
    c = x
    while c != 0 or len(sort_dict(c, dic).keys()) != 0:
        i = first_key_dic(max_dict(c, sort_dict(c, dic)))
        if i is None or i == 0:
            lst_dic_kq.append(0)
            break
        else:
            lst_dic_kq.append(i)
            c = c - first_vale_dic(max_dict(c, sort_dict(c, dic)))
            del dic[i]
    return lst_dic_kq


# -----------------------------------------------------
# Import dữ liệu excel
ps_Tang = pd.read_csv('ps_Tang.csv', header=None)
ps_Giam = pd.read_csv('ps_Giam_.csv', header=None)

# Khởi tạo dicA và dicB chứa dữ liệu
dicA = dict()
dicB = dict()

# Nạp dữ liệu vào dicA và dicB
for T in range(1, 184):  # 184
    dicA[str(ps_Tang.at[T, 0])] = float(ps_Tang.at[T, 1])

for G in range(1, 388):  # 388
    dicB[str(ps_Giam.at[G, 0])] = float(ps_Giam.at[G, 1])

temp = dict()
ls_del_dicA = list()
ls_del_dicB = list()
ls_del_dic_temp1 = list()
ls_del_dic_temp2 = list()

# Khởi tạo mảng kết quả

ketQua = np.zeros((388, 5))
# ----------------------------------------------------------------------
# Lay du lieu giong nhau
i = 0
for key1 in dicA.keys():
    for key2 in dicB.keys():
        if dicA.get(key1) == dicB.get(key2):
            if key2 not in ls_del_dicB:
                # Đưa kết quả vào mảng
                ketQua[i, 0] = key1
                ketQua[i, 1] = key1
                ketQua[i, 2] = key2
                ketQua[i, 3] = dicA.get(key1)
                ketQua[i, 4] = dicB.get(key2)
                i += 1
                ls_del_dicA.append(key1)
                ls_del_dicB.append(key2)
                break

# Xóa dữ liệu khi đã tìm ra ở dicA và dicB

for j in ls_del_dicA:
    del dicA[j]

for j in ls_del_dicB:
    del dicB[j]

ls_temp = list()
ls_del_dicA.clear()
ls_del_dicB.clear()
ls = list()
# -------------------------------------------------------------
# Tim du lieu toi uu
if len(dicA.keys()) != 0 and len(dicB.keys()) != 0:
    for key1 in dicA.keys():
        for key2 in dicB.keys():
            if dicB.get(key2) <= dicA.get(key1):
                temp[key2] = dicB.get(key2)
        if len(temp.keys()) == 0:
            break
        else:
            ls = lst_key_ketQua(dicA.get(key1), temp)
            for ls1 in ls:
                if ls1 != 0:
                    ketQua[i, 0] = key1
                    ketQua[i, 1] = key1
                    ketQua[i, 2] = ls1
                    ketQua[i, 3] = dicA.get(key1)
                    ketQua[i, 4] = dicB.get(ls1)
                    i += 1
                    del dicB[ls1]
                else:
                    break
            ls_del_dicA.append(key1)
    temp.clear()
for key1 in ls_del_dicA:
    del dicA[key1]
ls_del_dicA.clear()
# ----------------------------------------------
# Lấy ra dữ liệu không có khoản nào tương ứng
if len(dicA.keys()) != 0:
    for key1 in dicA.keys():
        ketQua[i, 0] = key1
        ketQua[i, 1] = key1
        ketQua[i, 2] = 0
        ketQua[i, 3] = dicA.get(key1)
        ketQua[i, 4] = 0
        i += 1
if len(dicB.keys()) != 0:
    for key2 in dicB.keys():
        ketQua[i, 0] = 0
        ketQua[i, 1] = 0
        ketQua[i, 2] = key2
        ketQua[i, 3] = 0
        ketQua[i, 4] = dicB.get(key2)
        i += 1

# ----------------------------------------------
# Xuất dữ liệu ra excel
df = pd.DataFrame(ketQua)
writer = pd.ExcelWriter('pandas_simple.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
