## SOAL NO 1


n = int(input("Masukkan ukuran sisi belah ketupat (N): "))
karakter = input("Masukkan karakter pilihan klien (seperti X atau O): ")

# Loop untuk bagian atas dan tengah belah ketupat
for i in range(n):
    # Cetak spasi
    print(' ' * (n - i - 1), end='')
    # Cetak pola checkerboard dengan jarak
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(karakter, end='')
        else:
            print(' ', end='')  # Menambahkan spasi untuk pola checkerboard
    print()

# Loop untuk bagian bawah belah ketupat
for i in range(n - 2, -1, -1):
    # Cetak spasi
    print(' ' * (n - i - 1), end='')
    # Cetak pola checkerboard dengan jarak
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(karakter, end='')
        else:
            print(' ', end='')  # Menambahkan spasi untuk pola checkerboard
    print()
