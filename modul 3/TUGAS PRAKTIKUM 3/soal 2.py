#meminta pengguna untuk memasukkan angka 
angka =input("Masukkan angka: ")

#variabel untuk menyimpan hasil kebalikn 
kebalikan =""

#menggunakan for dan range untuk membalik angka
for i in range(len(angka) -1, -1, -1): #mulai dari indeks terakhir ke indeks pertama
    kebalikan += angka[i]

print("Angka setelah dibalik:", kebalikan)
