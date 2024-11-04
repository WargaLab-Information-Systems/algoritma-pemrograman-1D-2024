n = int(input("masukkan ukuran n:"))
print()

for i in range (n):
    for y in range (n, i, -1):
        print(" ", end="")
    for y in range (2*i + 1):
        print("x", end="")
    print()
for i in range (n-2, -1, -1):
    for y in range (n, i, -1):
        print(" ", end="")
    for y in range (2*i + 1):
        print("x", end="")
    print()
