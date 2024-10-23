while True:
    rental = int(input("berapa hari anda rental DVD disini ? "))

    if rental <= 5:
        print("anda tidak perlu membayar denda")
        # break
    elif rental > 5:
        denda = (rental - 5) * 2500

        denda2 = 0
    elif rental > 10:
            denda2 = ((rental - 10) // 5) * 5500

    total_denda = denda + denda2
    print(f"Total denda yang harus dibayar: Rp.{total_denda:,}")

    juminten = input("apakah anda ingin menghitung kembali? (iya/tidak): ")
    if juminten != "iya":
        break