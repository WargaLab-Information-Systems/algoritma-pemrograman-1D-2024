N = int(input("Masukkan ukuran sisi: "))
karakter = input("Masukkan karakter pola (misalnya X atau O): ")

# Iterasi untuk setiap baris dalam belah ketupat
for i in range(1 - N, N):
    # Menghitung jumlah spasi di awal setiap baris
    if i < 0:
        spasi = -i
        row_width = N + i
    else:
        spasi = i
        row_width = N - i

    # Mencetak spasi untuk penyelarasan
    print(" " * spasi, end="")

    # Membuat pola checkerboard pada baris
    for j in range(2 * row_width - 1):
        # Menentukan karakter yang akan dicetak berdasarkan pola checkerboard
        if j % 2 == 0:
            print(karakter, end="")
        else:
            print(" ", end="")
    print()
