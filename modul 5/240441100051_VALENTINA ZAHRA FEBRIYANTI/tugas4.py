def cek_palindrom(kata):
    # Membandingkan kata dengan kata yang dibalik
    return kata == kata[::] #slicing

# Meminta input dari pengguna
input_kata = input("Masukkan kata untuk dicek apakah palindrom: ")
if cek_palindrom(input_kata):
    print(f'"{input_kata}" adalah kata palindrom.')
else:
    print(f'"{input_kata}" bukan kata palindrom.')