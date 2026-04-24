def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua(n - 1)


n = int(input("Nhập số nguyên dương n: "))

if n < 0:
    print("Không tính được giai thừa cho số âm.")
else:
    print(f"{n}! =", giai_thua(n))