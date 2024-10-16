nama_mhs1 = "jaka"
skor_jaka = 1100
ipk_jaka = 3.5

nama_mhs2 = "Ida" 
skor_ida = 1000
ipk_ida = 3.5

skor_minimal = 1100
ipk_minimal = 3.0
#jaka
if skor_jaka > skor_minimal and ipk_jaka >= ipk_minimal:
    print(f"{nama_mhs1} tidak lulus persyaratan")
elif skor_jaka > skor_minimal and ipk_jaka >= ipk_minimal:
    print(f"{nama_mhs1} lulus persyaratan")
else:
    print(f"{nama_mhs1}")

#ida
if skor_ida < skor_minimal and ipk_ida >= ipk_minimal:
    print(f"{nama_mhs2} tidak lulus persyaratan")
elif skor_jaka < skor_minimal and ipk_ida >= ipk_minimal:
    print(f"{nama_mhs2} lulus persyaratan")
else:
    print(f"{nama_mhs2}")