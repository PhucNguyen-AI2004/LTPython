boi_13_19 = lambda n: n % 13 == 0 or n % 19 == 0

n = int(input("Nhập n: "))

if boi_13_19(n):
    print(n, "là bội số của 13 hoặc 19")
else:
    print(n, "không là bội số của 13 hoặc 19")