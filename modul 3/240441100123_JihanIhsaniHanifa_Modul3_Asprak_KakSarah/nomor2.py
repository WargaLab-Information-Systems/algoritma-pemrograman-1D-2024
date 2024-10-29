# meminta input angka dari pengguna
angka = input("masukkan angka bulat: ")

# membalik urutan angka menggunakan looping
angka_terbalik = ""  # memasukkan angka angka yang sudah terbalik
i = len (angka) - 1 # -1 untuk mengambil angka paling belakang

while i >= 0:  
    angka_terbalik += angka[i]
    i -= 1

# menampilkan hasil
print("angka setelah dibalik: ",angka_terbalik)