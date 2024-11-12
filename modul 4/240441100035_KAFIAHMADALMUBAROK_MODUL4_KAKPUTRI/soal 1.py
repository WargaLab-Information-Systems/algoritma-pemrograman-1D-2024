karakter = input("Masukkan karakter (misalnya 'X' atau 'O'): ").lower()
N = int(input("Masukkan ukuran sisi (N): "))

# Bagian atas belah ketupat (garis tengah)
for i in range(N):
    print(' ' * (N - i - 1), end='')  # Spasi awal tiap baris
    for j in range(2 * i + 1): # kolom baris i +
        print(karakter if j % 2 == 0 else ' ', end='')  # kolom genap ganjil
    print()  

# Bagian bawah belah ketupat
for i in range(N - 2, -1, -1): 
    print(' ' * (N - i - 1), end='')  # Spasi awal tiap baris
    for j in range(2 * i + 1):
        print(karakter if j % 2 == 0 else ' ', end='')  
    print()  