so_chinh_phuong = lambda n: n >= 0 and int(n ** 0.5) ** 2 == n

n = int(input("Nhập n: "))

if so_chinh_phuong(n):
    print(n, "là số chính phương")
else:
    print(n, "không là số chính phương")