# Tạo dicA chứa dữ liệu phải thu.
# Tạo dicB chứa dữ liệu phải trả.
import numpy as np
import pandas as pd
import collections
ps_Tang = pd.read_csv('ps_Tang.csv', header=None)
ps_Giam = pd.read_csv('ps_Giam_.csv', header=None)

dicA = dict()
dicB = dict()
for i in range(1, 184):  # 184
    dicA[str(ps_Tang.at[i, 0])] = float(ps_Tang.at[i, 1])

for i in range(1, 388):  # 388
    dicB[str(ps_Giam.at[i, 0])] = float(ps_Giam.at[i, 1])


temp = dict()
ls_del_dicA = list()
ls_del_dicB = list()
ls_del_dic_temp1 = list()
ls_del_dic_temp2 = list()

# Khởi tạo mảng kết quả

ketQua = np.zeros((559, 5))

# Lay du lieu giong nhau
i = 0
for key1 in dicA.keys():
    for key2 in dicB.keys():
        if dicA.get(key1) == dicB.get(key2):
            if (key2 not in ls_del_dicB):
                # temp[key1] = dicA.get(key1)
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

for key1 in dicA.keys():
    for key2 in dicB.keys():
        if dicB.get(key2) < dicA.get(key1):
            temp[key2] = dicB.get(key2)
    if len(temp.keys()) > 1:
        a = 0
        for key3 in temp.keys():
            a += temp.get(key3)
            b = dicA.get(key1)
            c = b - a
            ls_temp.append(key3)
            if c == 0:
                for ls2 in ls_temp:
                    ketQua[i, 0] = key1
                    ketQua[i, 1] = key1
                    ketQua[i, 2] = ls2
                    ketQua[i, 3] = dicA.get(key1)
                    ketQua[i, 4] = temp.get(ls2)
                    i += 1
                    del dicB[ls2]
                ls_del_dic_temp2.append(key1)
                break
            elif c <= 1000000 and c >= -1000000:
                for ls2 in ls_temp:
                    ketQua[i, 0] = key1
                    ketQua[i, 1] = key1
                    ketQua[i, 2] = ls2
                    ketQua[i, 3] = dicA.get(key1)
                    ketQua[i, 4] = temp.get(ls2)
                    i += 1
                    del dicB[ls2]
                ls_del_dic_temp2.append(key1)
                break
        temp.clear()
        ls_temp.clear()
    else:
        for key3 in temp.keys():
            if dicA.get(key1) - temp.get(key3) >= -1000000 and dicA.get(key1) - temp.get(key3) <= 1000000:
                ketQua[i, 0] = key1
                ketQua[i, 1] = key1
                ketQua[i, 2] = key3
                ketQua[i, 3] = dicA.get(key1)
                ketQua[i, 4] = temp.get(key3)
                i += 1
                del dicB[key3]
                ls_del_dic_temp1.append(key1)
                temp.clear()
                break
temp.clear()

for key1 in ls_del_dic_temp1:
    del dicA[key1]
ls_del_dic_temp1.clear()

for key1 in ls_del_dic_temp2:
    del dicA[key1]
ls_del_dic_temp2.clear()

dicA1 = collections.OrderedDict(sorted(dicA.items(), key=lambda t: t[1]))
dicB1 = collections.OrderedDict(sorted(dicB.items(), key=lambda t: t[1]))


# ---------------------------------------------------------------------------------------------------------------
key1 = 0
key2 = 0
key3 = 0
if len(dicA.keys()) != 0 and len(dicB.keys()) != 0:
    for key1 in dicA1.keys():
        for key2 in dicB1.keys():
            temp[key2] = dicB1.get(key2)
            a = 0
            for key3 in temp.keys():
                a += temp.get(key3)
                b = dicA1.get(key1)
                c = b - a
                ls_temp.append(key3)
                if c == 0 or (c <= 100000 and c >= -100000):
                    ls_del_dic_temp1.append(key1)
                    for ls2 in ls_temp:
                        ketQua[i, 0] = key1
                        ketQua[i, 1] = key1
                        ketQua[i, 2] = ls2
                        ketQua[i, 3] = dicA1.get(key1)
                        ketQua[i, 4] = temp.get(ls2)
                        i += 1
                        del dicB[ls2]
                        ls_temp.clear()
                        break
        temp.clear()
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

# print(ketQua[0, 3])
# fobj = open('ngochung.txt', mode='a+')
# for i in range(0, 560):
#     for j in range(0, 5):
#         fobj.write(str(ketQua[i, j]))
# fobj.close()
# for i in range(0, 3):
#     for j in range(0, 5):
#         print(ketQua[i, j])
df = pd.DataFrame(ketQua)
writer = pd.ExcelWriter('pandas_simple.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
