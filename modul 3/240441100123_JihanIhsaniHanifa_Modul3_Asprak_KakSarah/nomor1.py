size = int(input("Masukkan Size: "))

# Angka 1
for i in range(size):
    print("x")
# Pindah baris
print()

# Angka 2
for i in range(size):
    if i == 0 or i == size-1 or i == size//2:
        print("X" * size)
    elif i < size // 2:
        print(" " * (size - 1) + "X")
    else:
        print("X")

# Pindah baris
print()

# Angka 3
for i in range(size):
    if i == 0 or i == size-1 or i == size//2:
        print("X" * size)
    else:
        print(" " * (size - 1) + "X")