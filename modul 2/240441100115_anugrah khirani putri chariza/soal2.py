mahasiswa_1 = "Jaka"
mahasiswa_2 = "Ida"

# Diketahui skor Jaka
skor_jaka = 1100
ipk_jaka = 3.5

# Diketahui skor Ida
skor_ida = 1000
ipk_ida = 3.5

# Syarat skor
syarat_skor = 1100
syarat_ipk = 3.0

# Perintah if else untuk Jaka
if skor_jaka > syarat_skor and ipk_jaka >= syarat_ipk:
    print(f"{mahasiswa_1} lulus Beasiswa")
else:
    print(f"{mahasiswa_1} tidak lulus Beasiswa karena nilainya kurang")

# Perintah if else untuk Ida
if skor_ida > syarat_skor and ipk_ida >= syarat_ipk:
    print(f"{mahasiswa_2} lulus Beasiswa")
else:
    print(f"{mahasiswa_2} tidak lulus Beasiswa karena nilainya kurang")