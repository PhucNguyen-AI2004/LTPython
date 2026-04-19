n = int(input("Nhập số nguyên dương n: "))

tam = n
la_so_may_man = True

while tam > 0:
    chu_so = tam % 10

    if chu_so != 6 and chu_so != 8:
        la_so_may_man = False
        break

    tam = tam // 10

if la_so_may_man:
    print(n, "là số may mắn")
else:
    print(n, "không phải số may mắn")