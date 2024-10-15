# Meminta input ukuran size
size = int(input("Masukan Size (harus lebih dari 3): "))

# Mengecek jika size kurang dari 3
if size < 3:
    print("Size harus lebih dari 3.")
else:
    # Cetak angka 0
    for i in range(size):
        if i == 0 or i == size - 1:
            print("0" * size)
        else:
            print("0" + " " * (size - 2) + "0")
    print()

# Cetak angka 3
    for i in range(size):
        if i == 0 or i == size - 1 or i == size // 2:
            print("3" * size)
        elif i < size // 2:
            print(" " * (size - 1) + "3")   # Space di akhir untuk bentuk 3
        else:
            print(" " * (size - 1) + "3")         # Space di depan untuk bentuk 3
    print()

    # Cetak angka 1
    for i in range(size):
        if i == 0:
            print(" " * (size // 2) + "1")  # Cetak 1 di tengah atas
        else:
            print(" " * (size // 2) + "1")  # Cetak 1 di tengah bawah
    print()