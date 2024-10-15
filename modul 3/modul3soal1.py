# jawaban soal nomor 1
# membuat bentuk angka nim terakhir 

print("Nim akhir adalah 043")
z = int(input("masukkan ukuran untuk nim yang anda inginkan: "))

# simbol angka untuk 0
for i in range(1, z + 1, 1):
    if i == 1:
        print("0" * z)
    if i < z:
        print("0" + " " * (z - 2) + "0")
    if i == z:
        print("0" * z)
        print()


# simbol angka untuk 4
for y in range(1, z + 1, 1):
    if y <= z // 2:
        print("0" + " " * (z - 2) + "0")
    if y == z // 2:
        print("0" * z)
    if y >= z // 2:
        print(" " * (z - 1) + "0")
        print()

# simbol angka untuk 3
for x in range(1, z + 1, 1):
    if x == 1:
        print("0" * z)
    if x < z // 2:
        print(" " * (z - 1) + "0")
    if x == z // 2:
        print("0" * z)
    if x > (z // 2) + 1:
        print(" " * (z - 1) + "0")
    if x == z:
        print("0" * z)
        print()
