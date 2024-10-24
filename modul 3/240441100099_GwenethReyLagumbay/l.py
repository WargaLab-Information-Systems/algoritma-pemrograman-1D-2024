# meminta input ukuran pola dari pengguna
size = int(input("masukkan ukuran pola"))

# NIM terakhir
nim = "099"

# pola untuk digit pertama '0'
for i in range(size):
    if i == 0 or i == size -1:
        print("0" * size)
    else:
        print("0" + " " * (size -2) + "0")

print ()

# pola untuk digit angka kedua '9'
for i in range(size):
    if i == 0 or i == size // 2 or i == size -1:
        print("9" + " " * (size -2) + "9")
    else:
        print(" " * (size -1) + "9")

print()

# pola untuk digit angka ketiga '9'
for i in range(size):
    if i == 0 or i == size // 2 or i == size -1:
        print("9" + " " * (size -2) + "9")
    else:
        print(" " * (size -1) + "9")