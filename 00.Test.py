import pandas as pd

df = pd.read_csv('HoaDonSuDung.csv')

SuDung = df['HoaDon']
ChuoiSuDung = []

PhatHanh = [k for k in range(1,10)]

for i in range(0,len(SuDung)):
    ChuoiSuDung.append(df['HoaDon'][i])

XoaBo = []
for j in range(0,len(PhatHanh)):
    if PhatHanh[j] not in ChuoiSuDung:
        XoaBo.append(PhatHanh[j])
print(XoaBo)