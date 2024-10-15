size = int(input("Masukkan angka= "))

# angka 0
for b in range (size):
    for k in range (size // 1):
        if b == 0 or b == size - 1 or k == 0 or k == (size // 1) - 1 :
            print("+", end="")
        else:
            print(" ", end="")
    print()
print() # spasi antar angka 

#angka 2
for b in range (size):
    for k in range (size // 1):
        if b == 0 or b == size // 2 or b == size - 1 or b == size // 1 or k == size // 1 - 1 and b < size // 2 or k == 0 and b > size // 2 :
            print("*", end="")
        else:
            print(" ", end="")
    print()

#angka 7
for b in range (size):
    for k in range (size // 1):
        if b == 0 or k == size - 1 :
            print("x", end="")
        else:
            print(" ", end="")
    print()        