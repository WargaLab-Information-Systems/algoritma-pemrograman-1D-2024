N = int(input("Masukkan ukuran sisi N: "))
karakter = input("Masukkan karakter pilihan (misal 'X' atau 'O'): ")

# Memastikan karakter yang dimasukkan adalah 'X' atau 'O'
while karakter != "X" and karakter != "O":
    karakter = input("Mohon masukkan karakter pilihan (X atau O): ")

total_baris = 2 * N - 1

for i in range(total_baris):
    if i < N:
        spasi = N - i - 1
    else:
        spasi = i - N + 1
    for j in range(total_baris):
        if (j >= spasi and j < total_baris - spasi) and ((i + j) % 2 == 0):
            print(karakter, end="")
        else:
            print(" ", end="")
    print()