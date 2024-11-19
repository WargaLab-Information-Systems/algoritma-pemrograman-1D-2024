n = int(input("Masukkan ukuran sisi (N): "))
karakter = input("Masukkan karakter pilihan (misal 'x' atau 'O'): ")


for i in range(n):
    print(" " * (n - i - 1), end="")
    print((karakter + " ") * (i + 1))

for i in range(n - 1):
    print(" " * (i + 1), end="")
    print((karakter + " ") * (n - i - 1))


