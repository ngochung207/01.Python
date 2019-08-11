# Tính ra số tiền bảo hiểm phải nộp của người lao động từ Mức lương cơ bản.
def BaoHiem(LuongCoBan):
	BaoHiem = LuongCoBan * 0.105
	return BaoHiem
# Tính ra tiền thuế TNCN từ thu nhập tính thuế.
def TienThueTNCN(TNTT):
	if TNTT <= 5000000:
		TienThueTNCN = 0.05 * TNTT
		return TienThueTNCN
	elif TNTT <= 10000000:
		TienThueTNCN = 0.1 * TNTT - 250000
		return TienThueTNCN
	elif  TNTT <= 18000000:
		TienThueTNCN = 0.15 * TNTT - 750000
		return TienThueTNCN
	elif TNTT <= 32000000:
		TienThueTNCN = 0.20 * TNTT - 1650000
		return TienThueTNCN
	elif TNTT <= 52000000:
		TienThueTNCN = 0.25 * TNTT - 3250000
		return TienThueTNCN
	elif TNTT <= 80000000:
		TienThueTNCN = 0.30 * TNTT - 5850000
		return TienThueTNCN
	else:
		TienThueTNCN = 0.35 * TNTT - 9850000
		return TienThueTNCN
def ThuNhapTinhThue(Tien):
	if Tien <= 5000000:
		ThuNhapTinhThue = Tien/0.95
		return ThuNhapTinhThue
	elif Tien <= 10000000:
		ThuNhapTinhThue = (Tien-250000)/0.9
		return ThuNhapTinhThue
	elif Tien <= 18000000:
		ThuNhapTinhThue = (Tien-750000)/0.85
		return ThuNhapTinhThue
	elif Tien <= 32000000:
		ThuNhapTinhThue = (Tien-1650000)/0.8
		return ThuNhapTinhThue
	elif Tien <= 52000000:
		ThuNhapTinhThue = (Tien-3250000)/0.75
		return ThuNhapTinhThue
	elif Tien <= 80000000:
		ThuNhapTinhThue = (Tien-5850000)/0.7
		return ThuNhapTinhThue
	else:
		ThuNhapTinhThue = (Tien-9850000)/0.65
		return ThuNhapTinhThue
# Tính ra mức lương Gross từ mức lương Net thực chi.
def LuongGross(ThucNhan, LuongCoBan, SoNguoiPhuThuoc):

	TienBaoHiem = BaoHiem(LuongCoBan)

	GiamTru = SoNguoiPhuThuoc * 3600000 + 9000000

	# (ThucNhan - GiamTru) --> tinh ra muc thu nhap tinh thue
	LuongGross = ThucNhan + TienBaoHiem + TienThueTNCN(ThuNhapTinhThue(max(ThucNhan - GiamTru,0)))
	
	while True:
		
		SaiSo = ThucNhan - (LuongGross - TienThueTNCN(max(LuongGross - TienBaoHiem - GiamTru,0)) - TienBaoHiem)
		if SaiSo >= -1 and SaiSo <= 1:
			LuongGross += SaiSo
			break
		else:
			LuongGross += 1
	return LuongGross

# Ví dụ test công thức
print(LuongGross(80000000,4000000,1))
