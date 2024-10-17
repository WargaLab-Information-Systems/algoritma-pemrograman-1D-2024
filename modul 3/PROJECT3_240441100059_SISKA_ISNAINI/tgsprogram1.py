# n Mengatur ukuran 
n = 6
# Loop untuk mencetak pola angka 0
# i == 0 (baris pertama)
# i == n-1 (baris terakhir)
# ii == 0 (kolom pertama)
# ii == n-1 (kolom terakhir)
for i in range(n):
    for ii in range(n):
        # Menentukan posisi di mana angka 0 harus dicetak
        if (i == 0 or i == n-1 or ii == 0 or ii == n-1):
            print("z", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# untuk mencetak pola angka 5
# i == 0: Membentuk garis horizontal di baris pertama.
# i == n//2: Membentuk garis horizontal di baris tengah.
# i == n-1: Membentuk garis horizontal di baris terakhir.
# (ii == 0 and i < n//2): Membentuk garis vertikal di kolom pertama dari baris pertama hingga baris tengah.
# (ii == n-1 and i > n//2): Membentuk garis vertikal di kolom terakhir dari baris tengah hingga baris terakhir.
for i in range(n):
    for ii in range(n):
        # Menentukan posisi di mana angka 5 harus dicetak
        if (i == 0 or i == n//2 or i == n-1 or (ii == 0 and i < n//2) or (ii == n-1 and i > n//2)):
            print("z", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Loop untuk mencetak pola angka 9
# i == 0: Baris pertama.
# i == n // 2: Baris tengah.
# i == n - 1 and ii < n - 1: Baris terakhir, kecuali kolom terakhir.
# ii == n - 1 and i != 0 and i < n - 1: Kolom terakhir, kecuali baris pertama dan terakhir.
# ii == 0 and i < n // 2: Kolom pertama, untuk baris sebelum baris tengah.
for i in range(n):
    for ii in range(n):
        # Menentukan posisi di mana angka 9 harus dicetak
        if (i == 0 or i == n//2 or i == n-1 and ii < n-1 or (ii== n-1 and i != 0 and i < n) or (ii == 0 and i < n//2)):
            print("z", end=" ")
        else:
            print(" ", end=" ")
    print()
print()