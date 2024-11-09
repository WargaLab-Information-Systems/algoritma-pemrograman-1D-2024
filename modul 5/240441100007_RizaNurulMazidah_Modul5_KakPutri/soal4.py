def cek_palindrom(kata):
    return kata == kata[::-1]

while True:
    # Meminta input dari pengguna
    input_kata = input("Masukkan kata untuk dicek apakah palindrom: ")
    
    # Mengecek apakah kata adalah palindrom
    if cek_palindrom(input_kata):
        print(f'"{input_kata}" adalah kata palindrom.')
    else:
        print(f'"{input_kata}" bukan kata palindrom.')
    
    # Menanyakan apakah ingin mengulang
    ulang = input("Ingin mengecek ulang? (ya/tidak): ")
    if ulang != "ya":
        break
