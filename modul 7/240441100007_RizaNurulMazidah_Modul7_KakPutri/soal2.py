# membuat dua set yang berisi nama siswa yang mengikuti klub Basket dan Renang.
klub_basket = {"wildan", "andre", "dika", "rian", "putra"}
klub_renang = {"wildan", "andre", "rehan", "agus", "firman"}

# menampilkan daftar siswa yang mengikuti kedua klub.
siswa_yang_mengikuti_kedua_klub = klub_basket.intersection(klub_renang)
print("siswa yang mengikuti kedua klub adalah:", (siswa_yang_mengikuti_kedua_klub))

# menampilkan daftar siswa yang hanya mengikuti satu klub saja.
siswa_yang_mengikuti_satu_klub = klub_basket.difference(klub_renang), klub_renang.difference(klub_basket)
print("siswa yang hanya mengikuti satu klub adalah:", (siswa_yang_mengikuti_satu_klub))

# menampilkan daftar semua siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut.
daftar_semua_siswa = klub_basket.union(klub_renang)
print("daftar semua siswa yang mengikuti klub basket dan klub renang:", (daftar_semua_siswa))

# menampilkan jumlah siswa unik yang mengikuti setidaknya satu dari kedua klub tersebut.
jumlah_semua_siswa =len (klub_basket.union(klub_renang))
print("jumlah semua siswa yang mengikuti klub renang dan klub basket:", (jumlah_semua_siswa))