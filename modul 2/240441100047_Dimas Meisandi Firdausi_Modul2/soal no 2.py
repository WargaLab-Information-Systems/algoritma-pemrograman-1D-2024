## SOAL NO 2
#  Memasukkan data Jaka dan Ida ke variabel yang sesuai
nama_jaka = "Jaka"
skor_jaka = 1100
ipk_jaka = 3.5

nama_ida = "Ida"
skor_ida = 1000
ipk_ida = 3.5

# Persyaratan beasiswa
skor_minimal = 1100
ipk_minimal = 3.0

# Pengecekan apakah Jaka memenuhi persyaratan beasiswa menggunakan struktur if-else
if skor_jaka > skor_minimal and ipk_jaka >= ipk_minimal:
    print(nama_jaka, "lulus persyaratan beasiswa.")
else:
    print(nama_jaka, "tidak lulus persyaratan beasiswa")

# Cek apakah Ida memenuhi persyaratan beasiswa menggunakan struktur if-else
if skor_ida > skor_minimal and ipk_ida >= ipk_minimal:
    print(nama_ida, "lulus persyaratan beasiswa.")
else:
    print(nama_ida, "tidak lulus persyaratan beasiswa.")
