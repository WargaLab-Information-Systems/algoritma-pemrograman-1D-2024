# soal 2
# persyaratan lulus
skor_minimal = 1100
ipk_minimal = 3.0

# data jaka
nama1 = "Jaka"
ipk_jaka = 3.5
skor_jaka = 1100

# cek kelulusan jaka
if skor_jaka >= skor_minimal and ipk_jaka >= ipk_minimal :
    print(f"Selamat {nama1} lulus beasiswa")
else : 
    print(f"Maaf {nama1}  belum lolos beasiswa")

# data ida
nama2 = "Ida"
ipk_ida = 3.0
skor_ida = 1000

# cek kelulusan ida
if skor_ida >= skor_minimal and ipk_ida >= ipk_minimal :
    print(f"Selamat {nama2} lulus beasiswa")
else  :
    print(f"Maaf {nama2} belum lolos beasiswa")
