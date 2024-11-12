def cek_palindrom(kata):
    # Menghapus spasi dan mengubah semua huruf menjadi kecil
    kata = kata.replace(" ", "").lower()
    
    # Membandingkan kata dengan kebalikannya
    return kata == kata[::-1]

while True:
    # Meminta input dari pengguna
    kata_input = input("Masukkan sebuah kata (atau ketik 'exit' untuk keluar): ")
    
    # Memeriksa apakah pengguna ingin keluar
    if kata_input.lower() == 'exit':
        print("Program dihentikan.")
        break
    
    # Memeriksa apakah kata tersebut palindrom
    if cek_palindrom(kata_input):
        print(f"{kata_input} adalah palindrom.")
    else:
        print(f"{kata_input} bukan palindrom.")