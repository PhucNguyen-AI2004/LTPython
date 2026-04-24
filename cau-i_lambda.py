phan_loai_tam_giac = lambda a, b, c: (
    "Không phải tam giác"
    if not (a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a)
    else "Tam giác đều"
    if a == b == c
    else "Tam giác vuông cân"
    if (a == b or a == c or b == c) and sorted([a, b, c])[0] ** 2 + sorted([a, b, c])[1] ** 2 == sorted([a, b, c])[2] ** 2
    else "Tam giác vuông"
    if sorted([a, b, c])[0] ** 2 + sorted([a, b, c])[1] ** 2 == sorted([a, b, c])[2] ** 2
    else "Tam giác cân"
    if a == b or a == c or b == c
    else "Tam giác thường"
)

a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

print(phan_loai_tam_giac(a, b, c))