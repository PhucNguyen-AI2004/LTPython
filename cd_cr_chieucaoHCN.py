chieudai = float(input(" Nhập chiều dài đáy hình chữ nhật (cm): " ))
chieurong = float(input(" Nhập chiều rộng đáy hình chữ nhật (cm): "))
chieucao = float(input(" Nhập chiều cao hình khối chữ nhật (cm): "))
decimal=2
dien_tich = chieudai * chieurong
the_tich = dien_tich * chieucao

print("Diện tích đáy hình chữ nhật = {0:.{2}f} cm²".format(dien_tich, the_tich, decimal))
print("Thể tích hình khối = {0:.{1}f} cm³".format(the_tich,decimal))



dai = eval(input(" Nhập chiều dài đáy hình chữ nhật (cm): " ))
rong = eval(input(" Nhập chiều rộng đáy hình chữ nhật (cm): "))
cao = eval(input(" Nhập chiều cao hình khối chữ nhật (cm): "))
decimal=2
dien_tich = dai * rong
the_tich = dien_tich * cao

print("Diện tích đáy hình chữ nhật = {0:.{2}f} cm²".format(dien_tich, the_tich, decimal))
print("Thể tích hình khối = {0:.{1}f} cm³".format(the_tich,decimal))