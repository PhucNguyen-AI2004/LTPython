n = int(input("Nhập số nguyên dương n: "))


solonnhat = 0

while n > 0:
    chu_so = n % 10
    if chu_so > solonnhat:
        solonnhat = chu_so
    n = n // 10

print("Chữ số lớn nhất là:", solonnhat)