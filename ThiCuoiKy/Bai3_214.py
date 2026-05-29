import math

la_so_nguyen_to = lambda n: n >= 2 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

la_so_chinh_phuong = lambda n: n >= 0 and int(math.sqrt(n)) ** 2 == n

la_tam_giac = lambda a, b, c: a + b > c and a + c > b and b + c > a


n = int(input("Nhập số nguyên n: "))

if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")

if la_so_chinh_phuong(n):
    print(n, "là số chính phương")
else:
    print(n, "không phải là số chính phương")
    
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

if la_tam_giac(a, b, c):
    print(a, b, c, "là 3 cạnh hợp lệ của tam giác")

    if a == b == c:
        print("Đây là tam giác đều")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        if a == b or a == c or b == c:
            print("Đây là tam giác vuông cân")
        else:
            print("Đây là tam giác vuông")
    elif a == b or a == c or b == c:
        print("Đây là tam giác cân")
    else:
        print("Đây là tam giác thường")
else:
    print(a, b, c, "không phải là 3 cạnh hợp lệ của tam giác")