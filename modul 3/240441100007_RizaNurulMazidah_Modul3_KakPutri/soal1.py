size = int(input("masukkan size : "))

#membuat angka 0
for i in range(size):
    for ii in range(size):
        if i == 0 or i == size - 1 or ii == 0 or ii == size - 1:
            print("0", end=" ")
        else:
            print(" ", end=" ")
    print()

#membuat angka 0
for i in range(size):
    for ii in range(size):
        if i == 0 or i == size - 1 or ii == 0 or ii == size - 1:
            print("0", end=" ")
        else:
            print(" ", end=" ")
    print()

#membuat angka 7
for i in range(size):
    for ii in range(size):
        if i == 0 or i + ii == size - 1:
            print("7", end=" ")
        else:
            print(" ", end=" ")
    print()