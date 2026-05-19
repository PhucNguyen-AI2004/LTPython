def la_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def xoay_so_mo_rong(n):
    bang = {
        '0': '0',
        '1': '1',
        '2': '2',
        '5': '5',
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


def la_strobogrammatic_mo_rong(n):
    return xoay_so_mo_rong(n) == n


for i in range(1000000):
    if la_strobogrammatic_mo_rong(i) and la_nguyen_to(i):
        print(i, end=" ")