so_nguyen_to = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

n = int(input("Nhập n: "))

if so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không là số nguyên tố")