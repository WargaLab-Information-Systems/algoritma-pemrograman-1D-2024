size = int(input("Masukkan Size: "))

for i in range(size):
    if i == 0:
        print(" " * (size - 2) + "xx")
    elif i < size - 1:
        print(" " * (size - 1) + "x")
    else:
        print(" " * (size - 2) + "xxx ")
print()

for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("x" * size)
    else:
        print(" " * (size - 1) + "x")
print()

for i in range(size):
    if i == 0 or i == size // 2 or i == size - 1:
        print("x" * size)
    elif i < size // 2:
        print("x" + " " * (size - 2) + "x")
    else:
        print(" " * (size - 1) + "x")