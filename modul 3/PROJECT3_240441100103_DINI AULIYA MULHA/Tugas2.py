    # Meminta input angka dari pengguna
angka = input("Masukkan angka bulat: ")

# Membalik urutan angka menggunakan looping
angka_terbalik = ""
i = len (angka) - 1

while i >= 0:
    angka_terbalik += angka[i]
    i -= 1
8
# Menampilkan hasil
print("Angka setelah dibalik: ",angka_terbalik)