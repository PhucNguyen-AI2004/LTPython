import math

dien_tich_hinh_tron = lambda r: math.pi * r * r

r = float(input("Nhập bán kính r: "))

print("Diện tích hình tròn là:", dien_tich_hinh_tron(r))