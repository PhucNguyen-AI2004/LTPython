def tao_strobogrammatic_mo_rong(n, tong_do_dai):
    if n == 0:
        return [""]

    if n == 1:
        return ["0", "1", "2", "5", "8"]

    danh_sach_giua = tao_strobogrammatic_mo_rong(n - 2, tong_do_dai)

    ket_qua = []

    for giua in danh_sach_giua:
        if n != tong_do_dai:
            ket_qua.append("0" + giua + "0")

        ket_qua.append("1" + giua + "1")
        ket_qua.append("2" + giua + "2")
        ket_qua.append("5" + giua + "5")
        ket_qua.append("6" + giua + "9")
        ket_qua.append("8" + giua + "8")
        ket_qua.append("9" + giua + "6")

    return ket_qua


n = int(input("Nhap n: "))

print("Cac so strobogrammatic mo rong gom", n, "chu so la:")
ds = tao_strobogrammatic_mo_rong(n, n)

for x in ds:
    print(x, end=" ")