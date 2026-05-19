def xoay_so(n):
    bang = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    s = str(n)
    kq = ""

    for chu_so in s[::-1]:
        if chu_so not in bang:
            return None
        kq += bang[chu_so]

    return int(kq)


def la_strobogrammatic(n):
    return xoay_so(n) == n


for i in range(1000000):
    if la_strobogrammatic(i):
        print(i, end=" ")