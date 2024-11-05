size = int(input("Masukkan ukuran: "))

# Cetak angka 0
for i in range(size):
    if i == 0 or i == size - 1:
        print("x" * size)  # Baris pertama dan terakhir penuh dengan 'x'
    else:
        print("x" + " " * (size - 2) + "x")  # Baris tengah ada 'x' di kedua ujung

print()  # Baris kosong sebagai pemisah

# Cetak angka 1
i = 0
while i < size:
    if i == 0:
        print(" " * (size - 2) + "x")  # Baris pertama, 'x' di paling kanan
    elif i == 1:
        print(" " * (size - 3) + "xx")  # Baris kedua, dua 'x' di dekat kanan
    else:
        print(" " * (size - 2) + "x")  # Baris lainnya, 'x' di paling kanan
    i += 1

print()  # Baris kosong sebagai pemisah

# Cetak angka 5
for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("x" * size)  # Baris pertama, tengah, dan terakhir penuh dengan 'x'
    elif i < size // 2:
        print("x")  # Baris sebelum tengah hanya 'x' di kiri
    else:
        print(" " * (size - 1) + "x")  # Baris setelah tengah, 'x' di kanan