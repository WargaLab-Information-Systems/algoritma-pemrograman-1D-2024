NIM = 103

size = int(input("Masukkan ukuran pola: "))

for i in range(size):
    if i == 0:
        print(" " * (size - 1) + "1")
    else:
        print(" " * (size - 1) + "1")

print()

for i in range(size):
    if i == 0 or i == size - 1:
        print("0" * size)
    else:
        print("0" + " " * (size - 2) + "0")

print()

for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("3" * size)
    else:
        print(" " * (size - 1) + "3")