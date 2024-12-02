siswa_basket = {"amina", "alivia", "novi", "lisa", "hida"}
siswa_renang = {"amina", "agus", "junaidi", "suhaimin", "hida"}
print("Siswa yang mengikuti klub Basket:", siswa_basket)
print("Siswa yang mengikuti klub Renang:", siswa_renang)

siswa_kedua_klub = siswa_basket.intersection(siswa_renang)
print("\nSiswa yang mengikuti kedua klub (Basket dan Renang):", siswa_kedua_klub)

siswa_satu_klub = siswa_basket.symmetric_difference(siswa_renang)
print("\nSiswa yang hanya mengikuti satu klub saja:", siswa_satu_klub)

semua_siswa = siswa_basket.union(siswa_renang)
print("\nSemua siswa unik yang mengikuti setidaknya satu klub:", semua_siswa)

jumlah_siswa_unik = len(semua_siswa)
print("\nJumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)
