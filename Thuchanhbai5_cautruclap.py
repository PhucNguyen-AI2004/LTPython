n= int(input(" nhập số nguyên dương n: "))

Tong = 0
Tich = 1

while n > 0:
    chu_so = n % 10
    Tong += chu_so
    Tich *= chu_so

    n = n // 10

print( " Tong = ", Tong)
print( " Tich = ", Tich)
