# Nhap vao so hoa don dau.
SoDau = int(input("Nhap vao so dau: "))
SoCuoi = int(input("Nhap vao so cuoi: "))

# Day so phat hanh
PhatHanh = {i for i in range(SoDau, SoCuoi + 1)}
slPhatHanh = len(PhatHanh)

# Day Su dung
SuDung = {1,2,3}
slSuDung = len(SuDung)

# Day xoa bo
XoaBo = PhatHanh - SuDung ''' Sai: truong hop hoa don chua su dung dang tinh la hoa don xoa bo, xem lai'''
slXoaBo = len(XoaBo)
# in ra ket qua
print('{:-^20}'.format("Ket Qua"))
print("So luong hoa don phat hanh: %s" %(slPhatHanh))
print("So luong hoa don su dung: %s" %(slSuDung))
print("So luong hoa don xoa bo: %s" %(slXoaBo))
print("Cac so xoa bo: %s" %(XoaBo))
