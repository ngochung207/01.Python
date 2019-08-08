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
# Tính ra mức lương Gross từ mức lương Net thực chi.
def LuongGross(ThucNhan, LuongCoBan, SoNguoiPhuThuoc):
	LuongGross = 0.9 * ThucNhan
	TienBaoHiem = BaoHiem(LuongCoBan)
	while True:
		TNTT = LuongGross - TienBaoHiem - SoNguoiPhuThuoc*3600000 - 9000000
		ThueTNCN = TienThueTNCN(TNTT)
		SaiSo = ThucNhan - (LuongGross - ThueTNCN - TienBaoHiem)
		if SaiSo >= -0.9 and SaiSo <= 0.9:
			break
		elif 0.3*LuongGross >= ThucNhan:
			break
		else:
			LuongGross += 1
	return LuongGross

# Ví dụ test công thức
print(LuongGross(15000000,9000000,1))