def cek_palindrom(kata):
    # Menghapus spasi dan mengubah semua huruf menjadi kecil
    kata = kata.replace(" ", "")
    
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

# Meminta input dari pengguna
kata_input = input("Masukkan sebuah kata: ")
# Memeriksa apakah kata tersebut palindrom
if cek_palindrom(kata_input):
    print(f"{kata_input} adalah palindrom.")
else:
    print(f"{kata_input} bukan palindrom.")