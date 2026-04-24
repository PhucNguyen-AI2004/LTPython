def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if a <= 0 or b <= 0:
    print("Vui lòng nhập hai số nguyên dương.")
else:
    print("Ước số chung lớn nhất là:", gcd(a, b))