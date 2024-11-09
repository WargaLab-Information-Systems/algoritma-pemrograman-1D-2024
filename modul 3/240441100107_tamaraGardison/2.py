# Meminta pengguna untuk memasukkan angka
angka =input("Masukkan angka: ")

# Variabel untuk menyimpan hasil kebalikan
kebalikan = ""

# Menggunakan for dan range untuk membalik angka
for i in range(len(angka) -1 , -1, -1):  # Mulai dari indeks terakhir ke indeks pertama
    kebalikan += angka[i]

print("Angka setelah dibalik:", kebalikan)

