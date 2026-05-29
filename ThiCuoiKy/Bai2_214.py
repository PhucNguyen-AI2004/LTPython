def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def dem_so_nguyen_to_nho_hon(n):
    dem = 0

    for i in range(2, n):
        if la_so_nguyen_to(i):
            dem += 1

    return dem


def uoc_so_la_nguyen_to(n):
    danh_sach = []

    for i in range(1, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            danh_sach.append(i)

    return danh_sach


n = int(input("Nhập số nguyên dương n: "))

if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")

print("Số lượng số nguyên tố nhỏ hơn", n, "là:", dem_so_nguyen_to_nho_hon(n))

print("Các ước số của", n, "là số nguyên tố:", end=" ")
ds = uoc_so_la_nguyen_to(n)

for x in ds:
    print(x, end=" ")