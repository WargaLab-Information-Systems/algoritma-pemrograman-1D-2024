#Meminta Input dari Pengguna
size = int(input("Masukkan ukuran: "))
karakter = str(input("Masukkan karakter (X atau O): "))

#Membuat Belah Ketupat
if karakter == "X" or karakter == "O":
    for i in range (1, size + 1):
        print(" " * (size - i) + (karakter + " ") * i)
    for i in range (size - 1, 0, -1):
        print(" " * (size - i) + (karakter + " ") * i)
else:
    print("Karakter tidak sesuai")