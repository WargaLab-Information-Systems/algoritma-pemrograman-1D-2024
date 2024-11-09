karakter = input("Masukkan karakter (X atau O): ")
N = int(input("Masukkan ukuran sisi belah ketupat: "))

# Bagian atas belah ketupat
for i in range(N):
    print(" " * (N-i-1) + karakter * (2*i+1))

# Bagian bawah belah ketupat
for i in range(N-2, -1, -1):
    print(" " * (N-i-1) + karakter * (2*i+1))
    