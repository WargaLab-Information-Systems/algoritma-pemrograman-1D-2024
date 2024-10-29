ukuran = int(input("Masukkan ukuran: "))
bentuk = input("Mau bentuk X atau O?: ")

for i in range(ukuran):
    for j in range(ukuran - i):
        print(" ", end="")
    for k in range(i + 1):
        print(f"{bentuk} ", end="")
    print()

for i in range(ukuran - 1):
    for j in range(i + 2):
        print(" ", end="")
    for k in range(ukuran - i - 1):
        print(f"{bentuk} ", end="")
    print()