size = int(input("Masukkan Size: "))

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("0", end="")
        else:
            print(" ", end="")
    print()


for i in range(size):
    if i == 0 or i == size-1 or i == size//2:
        print("8" * size)
    else:
        print("8" + " " * (size-2)+"8")





for i in range(size):
    if i == 0:
        print( "7" * size)
    else:
        print(" " * (size - i) + "7")