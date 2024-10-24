size = int(input("Masukkan size: "))

# Angka 1
for i in range(size):
    print("" * (size) + "x")
print()

#angka 3
for i in range (size):
    if i == 0 or i == size -1:
        print("x" * size)
    elif i == 3:
        print("x" * size)
    else:
        print("      x")
print ()

#angka 1
for i in range(size):
    print("" * (size) + "x")
print()