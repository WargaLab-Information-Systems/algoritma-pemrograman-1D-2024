# Program untuk membalikkan urutan angka

# Meminta input dari pengguna
angka = input("Masukkan angka bulat: ")

# Membalikkan urutan angka menggunakan slicing
for i in range(len(angka)-1,-1,-1):
    angka_terbalik = angka[::-1]
# Menampilkan hasil
print("Angka setelah dibalik:", angka_terbalik)
