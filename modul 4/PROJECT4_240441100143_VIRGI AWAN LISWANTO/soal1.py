while True:
    N = int(input("Masukkan ukuran sisi (N): "))
    total_ukuran = 2 * N - 1
    karakter = input("Masukkan karakter (misal 'X' atau 'O'): ")
    if karakter == "X" or karakter == "O":
        for i in range(total_ukuran):
            if i < N:
                spasi = N - 1 - i
            else:
                spasi = i - N + 1
            panjang_baris = total_ukuran - 2 * spasi
            baris = ""
            for j in range(panjang_baris):
                if (i + j) % 2 == 0:
                    baris += karakter
                else:
                    baris += ' '
            print(' ' * spasi + baris)
        print("Karakter sudah sesuai")
        break  
    else:
        print("Masukkan karakter yang sesuai (X atau O).")
