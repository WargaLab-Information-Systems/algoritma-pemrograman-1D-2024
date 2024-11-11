def cek_palindrom(kata):
    kata = kata.replace(" ", "")
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

# Contoh penggunaan fungsi
kata_input = input("Masukkan sebuah kata: ")
if cek_palindrom(kata_input):
    print(f'"{kata_input}" adalah palindrom.')
else:
    print(f'"{kata_input}" bukan palindrom.')