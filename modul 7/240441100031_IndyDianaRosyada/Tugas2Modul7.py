# Membuat set untuk siswa di klub Basket dan Renang
klub_basket = {"Damar", "Zavier", "Arona", "Alana"}
klub_renang = {"Zavier", "Alana", "Sigit", "Fani"}

# a. Menampilkan dua set
print("Siswa di Klub Basket:", klub_basket)
print("Siswa di Klub Renang:", klub_renang)

# b. Menampilkan daftar siswa yang mengikuti kedua klub
siswa_kedua_klub = klub_basket.intersection(klub_renang)
print("Siswa yang mengikuti kedua klub:", siswa_kedua_klub)

# c. Menampilkan daftar siswa yang hanya mengikuti satu klub saja
siswa_hanya_satu_klub = (klub_basket.difference(klub_renang)).union(klub_renang.difference(klub_basket))
print("Siswa yang hanya mengikuti satu klub:", siswa_hanya_satu_klub)

# d. Menampilkan daftar semua siswa unik
siswa_unik = klub_basket.union(klub_renang)
print("Semua siswa unik yang mengikuti setidaknya satu klub:", siswa_unik)

# e. Menampilkan jumlah siswa unik
jumlah_siswa_unik = len(siswa_unik) # len() untuk menghitung jumlah elemen dalam set siswa_unik
print("Jumlah siswa unik yang mengikuti setidaknya satu klub:", jumlah_siswa_unik)