size = int(input("Masukkan ukuran pola nim: "))

for row in range(size):
    for col in range(size):
        if (row == 0 or row == size - 1 or col == 0 or col == size - 1):
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

for row in range(size):
    for col in range(size):
        if col == size // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

for row in range(size):
    for col in range(size):
        if col == size // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
