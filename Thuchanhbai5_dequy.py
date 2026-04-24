def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập n là số nguyên dương.")
else:
    print(f"Số hạng Fibonacci thứ {n} là:", fibonacci(n))   