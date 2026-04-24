def tong_chu_so(n):
    if n == 0:
        return 0
    return n % 10 + tong_chu_so(n // 10)


n = int(input("Nhập số nguyên n: "))

# Nếu n âm thì đổi sang dương để tính tổng chữ số
n = abs(n)

print("Tổng các chữ số là:", tong_chu_so(n))