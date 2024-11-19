## SOAL NO 2


# set siswa yang mengikuti klub basket dan renang
klub_basket = {"Salman", "Dimas", "Xaviers", "Gatot", "Edi"}
klub_renang = {"Samsul", "Fania", "Salman", "Edi", "Ulhaq"}


#daftar siswa yang mengikuti kedua klub (irisan)
siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("\nSiswa yang mengikuti kedua klub:", siswa_kedua_klub)

#daftar siswa yang hanya mengikuti satu klub saja (simpangan)
siswa_satu_klub_saja = klub_basket.symmetric_difference(klub_renang)
print("\nSiswa yang hanya mengikuti satu klub saja:", siswa_satu_klub_saja)

# daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub (gabungan)
siswa_unik = klub_basket.union(klub_renang)
print("\nSemua siswa unik yang mengikuti setidaknya satu dari kedua klub:", siswa_unik)

# jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub (banyak siswa)
jumlah_siswa_unik = len(siswa_unik)
print("\nJumlah siswa unik yang mengikuti setidaknya satu dari kedua klub:", {jumlah_siswa_unik})
