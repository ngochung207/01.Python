# Nhập vào số đầu và số cuối của dẫy hóa đơn phát hành.
SoDau = int(input("Nhap vao so dau: "))
SoCuoi = int(input("Nhap vao so cuoi: "))

# Tạo ra chuỗi hóa đơn phát hành từ dữ liệu người dùng nhập.
ChuoiPhatHanh = [i for i in range(SoDau, SoCuoi + 1)]
slPhatHanh = len(ChuoiPhatHanh)

# Import dữ liệu từ file csv các hóa đơn sử dụng.
import pandas as pd
ListSuDung = pd.read_csv('HoaDonSuDung.csv')

# Tạo ra chuối hóa đơn sử dụng từ dữ liệu nhập vào.
ChuoiSuDung = []
for i in range(0, len(ListSuDung)):
    ChuoiSuDung.append(ListSuDung['HoaDon'][i])

# Đếm số lượng hóa đơn sử dụng.
slSuDung = len(ChuoiSuDung)


# Tìm vị trí của số hóa đơn lớn nhất của chuỗi hóa đơn sử dụng trong chuỗi hóa đơn phát hành.
SoChuaDung = ChuoiPhatHanh.index(max(ChuoiSuDung))
ChuoiChuaDung = ChuoiPhatHanh[SoChuaDung+1:None]


# Tìm các hóa đơn xóa bỏ
ChuoiXoaBo = []
for i in range(0, len(ChuoiPhatHanh[0:SoChuaDung+1])):
    if  ChuoiPhatHanh[i] not in ChuoiSuDung:
        ChuoiXoaBo.append(ChuoiPhatHanh[i])

slXoaBo = len(ChuoiXoaBo)

# In ra kết quả
print('{:-^80}'.format("Ket Qua"))
print("Chuoi phat hanh: %s" %ChuoiPhatHanh)
print("So luong hoa don phat hanh: %s" %slPhatHanh)
print("Chuoi su dung: %s" %ChuoiSuDung)
print("So luong hoa don su dung: %s" %slSuDung)
print("Chuoi xoa bo: %s" %ChuoiXoaBo)
print("So luong hoa don xoa bo: %s" %(slXoaBo))
print("Chuoi chua dung: %s" %ChuoiChuaDung)
print("So luong hoa don chua dung: %s" %len(ChuoiChuaDung))
'''
Các vấn đề chưa giải quyết được:
    1. Dãy nhập vào không theo thứ tự, thì ChuoiChuaSuDung sẽ bị lấy sai.
    2. Chưa giải quyết được bài toán 1 dãy phát hành có nhiều dải sử dụng.
'''